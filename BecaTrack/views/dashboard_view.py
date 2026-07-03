import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from views.components.kpi_card import KPICard
from services.dashboard_service import DashboardService
from config import COLOR_PALETTE

class DashboardView(ctk.CTkFrame):
    """Vista del Dashboard que contiene los KPIs y las gráficas interactivas."""
    
    def __init__(self, parent, dashboard_service: DashboardService):
        super().__init__(parent, fg_color="transparent")
        self.dashboard_service = dashboard_service
        self._setup_ui()
        self.load_data()

    def _setup_ui(self):
        # Contenedor superior para KPIs
        self.kpi_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.kpi_frame.pack(fill="x", pady=(0, 20))
        
        self.kpis = {}
        
        # Definición de las tarjetas
        titles = [
            ("Total Becarios", "total_students", "👥", COLOR_PALETTE["blue"]),
            ("Seguimientos", "total_trackings", "📝", COLOR_PALETTE["blue"]),
            ("Promedio Notas", "avg_grade", "⭐", COLOR_PALETTE["green"]),
            ("Asistencia", "attendance_rate", "✅", COLOR_PALETTE["green"]),
            ("En Riesgo", "at_risk_students", "⚠️", COLOR_PALETTE["red"]),
            ("Horas Vol.", "total_volunteer_hours", "🕒", COLOR_PALETTE["blue"])
        ]
        
        # Crear cuadrícula de KPIs
        for i, (title, key, icon, color) in enumerate(titles):
            card = KPICard(self.kpi_frame, title=title, value="0", icon=icon, color=color)
            card.grid(row=i//3, column=i%3, padx=15, pady=15)
            self.kpis[key] = card
            
        # Contenedor inferior para Gráficas
        self.charts_frame = ctk.CTkFrame(self, fg_color=COLOR_PALETTE["dark_gray"], corner_radius=15)
        self.charts_frame.pack(fill="both", expand=True, padx=15, pady=5)
        
        # Preparar Matplotlib (modo oscuro nativo)
        plt.style.use('dark_background')
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(10, 4))
        
        # Ajustar fondo de la figura para que coincida con CustomTkinter
        hex_color = COLOR_PALETTE["dark_gray"]
        self.fig.patch.set_facecolor(hex_color)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.charts_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=20, pady=20)
        
    def load_data(self):
        kpi_data = self.dashboard_service.get_kpis()
        
        # Actualizar Tarjetas
        for key, card in self.kpis.items():
            if key in kpi_data:
                val = kpi_data[key]
                if key == "attendance_rate":
                    val = f"{val}%"
                card.update_value(val)
                
        # Dibujar gráficas
        self._draw_charts(kpi_data)
        
    def _draw_charts(self, kpi_data):
        self.ax1.clear()
        self.ax2.clear()
        
        bg_color = COLOR_PALETTE["dark_gray"]
        self.ax1.set_facecolor(bg_color)
        
        # Gráfica 1: Asistencia (Pastel)
        labels = ['Asistió', 'No Asistió']
        rate = kpi_data.get('attendance_rate', 0)
        # Fallback por si rate es 0 para que no falle matplotlib
        if rate == 0:
            sizes = [0.1, 99.9]
        else:
            sizes = [rate, 100 - rate]
            
        colors = [COLOR_PALETTE["green"], COLOR_PALETTE["red"]]
        
        self.ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, textprops={'color':"w"})
        self.ax1.set_title("Tasa de Asistencia Global", color="white")
        
        # Gráfica 2: Estado Académico (Barras)
        self.ax2.set_facecolor(bg_color)
        risk = kpi_data.get('at_risk_students', 0)
        total = kpi_data.get('total_students', 0)
        safe = total - risk
        
        self.ax2.bar(['En Riesgo', 'Seguros'], [risk, safe], color=[COLOR_PALETTE["red"], COLOR_PALETTE["blue"]])
        self.ax2.set_title("Estado Académico de Becarios", color="white")
        self.ax2.tick_params(colors="white")
        
        # Ocultar bordes para diseño limpio
        for spine in self.ax2.spines.values():
            spine.set_visible(False)
            
        self.fig.tight_layout()
        self.canvas.draw()
