import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from views.components.kpi_card import KPICard
from services.dashboard_service import DashboardService
from config import COLOR_PALETTE

class DashboardView(ctk.CTkScrollableFrame):
    """Dashboard principal reconstruido con el tema claro, gráficas modernas y tabla inferior."""
    def __init__(self, parent, dashboard_service: DashboardService):
        super().__init__(parent, fg_color=COLOR_PALETTE["bg_app"], corner_radius=0)
        self.dashboard_service = dashboard_service
        self._setup_ui()
        self.load_data()

    def _setup_ui(self):
        self.grid_columnconfigure((0, 1, 2), weight=1)
        
        self.kpis = {}
        titles = [
            ("Total Becarios", "total_students", "↑ 12% desde el mes pasado", "👥", COLOR_PALETTE["blue_light"], COLOR_PALETTE["blue"]),
            ("Seguimientos Activos", "total_trackings", "↑ 5 nuevos hoy", "📄", COLOR_PALETTE["blue_light"], COLOR_PALETTE["blue"]),
            ("Promedio General", "avg_grade", "↑ 0.2 pts desde el mes pasado", "⭐", COLOR_PALETTE["green_light"], COLOR_PALETTE["green"]),
            ("Tasa de Asistencia", "attendance_rate", "Estable", "✅", COLOR_PALETTE["green_light"], COLOR_PALETTE["green"]),
            ("Estudiantes en Riesgo", "at_risk_students", "⚠️ Riesgo detectado", "⚠️", COLOR_PALETTE["red_light"], COLOR_PALETTE["red"]),
            ("Horas Voluntariado", "total_volunteer_hours", "🕒 Buen progreso", "🕒", "#FEF3C7", "#D97706")
        ]
        
        for i, (title, key, subtitle, icon, bg_color, fg_color) in enumerate(titles):
            card = KPICard(self, title=title, value="0", subtitle=subtitle, icon=icon, bg_icon_color=bg_color, icon_color=fg_color)
            card.grid(row=i//3, column=i%3, padx=10, pady=10, sticky="nsew")
            self.kpis[key] = card
            
        # Gráficas
        self.charts_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.charts_frame.grid(row=2, column=0, columnspan=3, sticky="nsew", pady=15)
        self.charts_frame.grid_columnconfigure((0, 1), weight=1)
        
        self.chart1_container = ctk.CTkFrame(self.charts_frame, fg_color=COLOR_PALETTE["bg_card"], corner_radius=15, border_width=1, border_color=COLOR_PALETTE["border"])
        self.chart1_container.grid(row=0, column=0, sticky="nsew", padx=10)
        
        self.chart2_container = ctk.CTkFrame(self.charts_frame, fg_color=COLOR_PALETTE["bg_card"], corner_radius=15, border_width=1, border_color=COLOR_PALETTE["border"])
        self.chart2_container.grid(row=0, column=1, sticky="nsew", padx=10)
        
        # Matplotlib estilo web
        plt.style.use('default')
        
        self.fig1, self.ax1 = plt.subplots(figsize=(5, 4))
        self.fig1.patch.set_facecolor(COLOR_PALETTE["bg_card"])
        self.canvas1 = FigureCanvasTkAgg(self.fig1, master=self.chart1_container)
        self.canvas1.get_tk_widget().pack(fill="both", expand=True, padx=20, pady=20)
        
        self.fig2, self.ax2 = plt.subplots(figsize=(5, 4))
        self.fig2.patch.set_facecolor(COLOR_PALETTE["bg_card"])
        self.canvas2 = FigureCanvasTkAgg(self.fig2, master=self.chart2_container)
        self.canvas2.get_tk_widget().pack(fill="both", expand=True, padx=20, pady=20)
        
        # Tabla Inferior (Fake por diseño)
        self.table_container = ctk.CTkFrame(self, fg_color=COLOR_PALETTE["bg_card"], corner_radius=15, border_width=1, border_color=COLOR_PALETTE["border"])
        self.table_container.grid(row=3, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)
        
        self.table_header = ctk.CTkFrame(self.table_container, fg_color="transparent")
        self.table_header.pack(fill="x", padx=20, pady=20)
        
        self.t_title = ctk.CTkLabel(self.table_header, text="Últimos Seguimientos Registrados", font=ctk.CTkFont(size=18, weight="bold"), text_color=COLOR_PALETTE["text_primary"])
        self.t_title.pack(side="left")
        
        self.new_reg_btn = ctk.CTkButton(self.table_header, text="+ Nuevo Registro", fg_color=COLOR_PALETTE["blue"], font=ctk.CTkFont(weight="bold"))
        self.new_reg_btn.pack(side="right")
        
        # Mock de tabla
        headers_frame = ctk.CTkFrame(self.table_container, fg_color="transparent")
        headers_frame.pack(fill="x", padx=20, pady=5)
        for h in ["ESTUDIANTE", "PROGRAMA", "FECHA", "ESTADO", "ACCIÓN"]:
            lbl = ctk.CTkLabel(headers_frame, text=h, text_color=COLOR_PALETTE["text_secondary"], font=ctk.CTkFont(weight="bold", size=12))
            lbl.pack(side="left", expand=True, anchor="w")
            
        row_frame = ctk.CTkFrame(self.table_container, fg_color="transparent")
        row_frame.pack(fill="x", padx=20, pady=10)
        ctk.CTkLabel(row_frame, text="Ana Martínez", font=ctk.CTkFont(weight="bold"), text_color=COLOR_PALETTE["text_primary"]).pack(side="left", expand=True, anchor="w")
        ctk.CTkLabel(row_frame, text="Ingeniería en Sistemas", text_color=COLOR_PALETTE["text_secondary"]).pack(side="left", expand=True, anchor="w")
        ctk.CTkLabel(row_frame, text="02 Jul 2026", text_color=COLOR_PALETTE["text_secondary"]).pack(side="left", expand=True, anchor="w")
        
        status_lbl = ctk.CTkLabel(row_frame, text="Al día", text_color=COLOR_PALETTE["green"], fg_color=COLOR_PALETTE["green_light"], corner_radius=10, width=60)
        status_lbl.pack(side="left", expand=True, anchor="w")
        
        action_lbl = ctk.CTkLabel(row_frame, text="Revisar", text_color=COLOR_PALETTE["blue"], font=ctk.CTkFont(weight="bold"))
        action_lbl.pack(side="left", expand=True, anchor="w")

    def load_data(self):
        kpi_data = self.dashboard_service.get_kpis()
        for key, card in self.kpis.items():
            if key in kpi_data:
                val = kpi_data[key]
                if key == "attendance_rate":
                    val = f"{val}%"
                card.update_value(val)
        self._draw_charts(kpi_data)
        
    def _draw_charts(self, kpi_data):
        self.ax1.clear()
        self.ax2.clear()
        
        # Dona de Asistencia
        rate = kpi_data.get('attendance_rate', 0)
        if rate == 0: rate = 85 # Visual mock
        sizes = [rate, 100 - rate]
        colors = [COLOR_PALETTE["blue"], COLOR_PALETTE["border"]]
        
        wedges, texts = self.ax1.pie(sizes, colors=colors, startangle=90, wedgeprops=dict(width=0.3, edgecolor=COLOR_PALETTE["bg_card"], linewidth=2))
        self.ax1.set_title("Tasa de Asistencia Global", color=COLOR_PALETTE["text_primary"], fontweight="bold", loc="left", pad=20)
        self.ax1.text(0, 0, f"{rate}%", ha='center', va='center', fontsize=24, fontweight='bold', color=COLOR_PALETTE["text_primary"])
        self.ax1.text(0, -0.2, "Asistencia", ha='center', va='center', fontsize=10, color=COLOR_PALETTE["text_secondary"])
        
        # Barras de Estado
        risk = kpi_data.get('at_risk_students', 0)
        total = kpi_data.get('total_students', 0)
        if total == 0:
            excelente, seguros, risk = 50, 40, 10
        else:
            excelente = total * 0.5
            seguros = total - risk - excelente
            
        bars = self.ax2.bar(['Excelentes', 'Seguros', 'En Riesgo'], [excelente, seguros, risk], color=[COLOR_PALETTE["green"], COLOR_PALETTE["blue"], COLOR_PALETTE["red"]], width=0.4)
        self.ax2.set_title("Estado Académico", color=COLOR_PALETTE["text_primary"], fontweight="bold", loc="left", pad=20)
        
        for spine in self.ax2.spines.values():
            spine.set_visible(False)
        self.ax2.tick_params(left=False, bottom=False)
        self.ax2.set_yticks([]) 
        
        self.fig1.tight_layout()
        self.fig2.tight_layout()
        self.canvas1.draw()
        self.canvas2.draw()
