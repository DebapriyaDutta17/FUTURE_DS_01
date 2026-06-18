import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.gridspec as gridspec
from matplotlib.patches import Rectangle

# 1. Load data and format date groupings
df = pd.read_csv("Sample_Business_Sales_Data.csv")
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Ensure chronological month sorting dynamically
df['MonthNum'] = df['OrderDate'].dt.month
df['Month'] = df['OrderDate'].dt.strftime('%b') # 3-letter tags prevent collision

# ---------------------------------------------------------
# HIGH-END EXECUTIVE NEON GLOW CONFIGURATION
# ---------------------------------------------------------
BG_COLOR = '#06060c'         # Dark backing for color contrast
CARD_BG = '#111124'          # Tile frame filling
BORDER_COLOR = '#2b1a4a'     # Panel edge accents
TEXT_MAIN = '#ffffff'        
TEXT_MUTED = '#727299'       

# Eye-Catching Multi-Color Corporate Palette
CYAN_GLOW = '#00f5d4'        # Vibrant Mint/Teal
PINK_GLOW = '#ff007f'        # Hot Electric Pink
PURPLE_GLOW = '#9b5de5'      # Bright Cyber Purple
ORANGE_GLOW = '#ff9f1c'      # Energetic Safety Orange
YELLOW_GLOW = '#fee440'      # Vivid Electric Yellow

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['text.color'] = TEXT_MAIN
plt.rcParams['axes.labelcolor'] = TEXT_MUTED
plt.rcParams['xtick.color'] = TEXT_MUTED
plt.rcParams['ytick.color'] = TEXT_MUTED

def style_card(ax):
    ax.set_facecolor(CARD_BG)
    for spine in ax.spines.values():
        spine.set_color(BORDER_COLOR)
        spine.set_linewidth(1.5)
    ax.tick_params(colors=TEXT_MUTED, labelsize=9)

# Master widescreen matrix canvas configuration with large vertical margins
fig = plt.figure(figsize=(24, 14), facecolor=BG_COLOR)
gs = gridspec.GridSpec(3, 4, figure=fig, height_ratios=[0.12, 0.44, 0.44], wspace=0.38, hspace=0.48)

# ---------------------------------------------------------
# HEADER SECTION
# ---------------------------------------------------------
fig.text(0.03, 0.96, '✦ EXECUTIVE RETRO-WAVE SALES INTELLIGENCE MATRIX', fontsize=26, fontweight='black', color=TEXT_MAIN)
fig.text(0.03, 0.93, 'REAL-TIME TRANSACTION CHANNELS • QUANTITY VOLUME ANALYSIS • MARGIN OPTIMIZATION', fontsize=11, color=CYAN_GLOW, fontweight='bold')
fig.text(0.74, 0.95, 'SYSTEM: STABLE  |  RETENTION: 100%  |  SCOPE: GLOBAL ANALYSIS', fontsize=10, color=TEXT_MUTED, fontfamily='monospace')

# ---------------------------------------------------------
# ROW 1: KPI SCORECARDS
# ---------------------------------------------------------
kpi_data = [
    {"label": "TOTAL CORE REVENUE", "val": f"${df['Sales'].sum():,.2f}", "color": CYAN_GLOW},
    {"label": "NET MARGIN PROFIT", "val": f"${df['Profit'].sum():,.2f}", "color": PINK_GLOW},
    {"label": "AVERAGE BASKET VALUE", "val": f"${df['Sales'].sum()/df['OrderID'].nunique():,.2f}", "color": PURPLE_GLOW},
    {"label": "GROSS UNITS SHIPPED", "val": f"{df['Quantity'].sum():,}", "color": YELLOW_GLOW}
]

for i, kpi in enumerate(kpi_data):
    ax = fig.add_subplot(gs[0, i], facecolor=CARD_BG)
    ax.set_xticks([])
    ax.set_yticks([])
    style_card(ax)
    
    rect = Rectangle((0,0), 0.02, 1, transform=ax.transAxes, color=kpi['color'])
    ax.add_patch(rect)
    
    ax.text(0.08, 0.68, kpi['label'], fontsize=10, color=TEXT_MUTED, fontweight='bold')
    ax.text(0.08, 0.25, kpi['val'], fontsize=24, fontweight='black', color=TEXT_MAIN)

# ---------------------------------------------------------
# ROW 2: PRIMARY CHARTS
# ---------------------------------------------------------
# Chart 1: Profit by Region (Horizontal Bars with dynamic padding limits)
ax1 = fig.add_subplot(gs[1, 0:2])
style_card(ax1)
reg_p = df.groupby('Region')['Profit'].sum().sort_values(ascending=True).reset_index()
bars1 = ax1.barh(reg_p['Region'], reg_p['Profit'], color=[PURPLE_GLOW, ORANGE_GLOW, PINK_GLOW, CYAN_GLOW], height=0.45)
ax1.set_title('PROFIT YIELD BY REGIONAL SALES CORRIDOR', fontsize=12, fontweight='bold', pad=20, color=CYAN_GLOW, loc='left')
ax1.xaxis.grid(True, linestyle=':', alpha=0.15, color=TEXT_MAIN)
ax1.yaxis.grid(False)
ax1.set_xlim(0, reg_p['Profit'].max() * 1.25)  # Extended margin to protect bar text labels from wall
ax1.bar_label(bars1, fmt='$%1.0f', padding=12, color=TEXT_MAIN, fontweight='bold', size=10)

# Chart 2: Category Allocation (Donut - Clean Legend Partitioning)
ax2 = fig.add_subplot(gs[1, 2])
style_card(ax2)
cat_q = df.groupby('Category')['Quantity'].sum()
wedges, texts, autotexts = ax2.pie(
    cat_q, labels=None, autopct='%1.0f%%', pctdistance=0.75,
    colors=[PURPLE_GLOW, PINK_GLOW, CYAN_GLOW], startangle=50,
    textprops=dict(color=TEXT_MAIN, fontsize=11, fontweight='bold'),
    wedgeprops=dict(width=0.45, edgecolor=BG_COLOR, linewidth=3)
)
ax2.legend(wedges, cat_q.index, loc="lower center", bbox_to_anchor=(0.5, -0.15), ncol=3, frameon=False, fontsize=9)
ax2.set_title('VOLUME ALLOCATION BY DEPARTMENT', fontsize=12, fontweight='bold', pad=20, color=CYAN_GLOW)

# Chart 3: Monthly Net Progress (Vertical Bars with sky ceiling buffer)
ax3 = fig.add_subplot(gs[1, 3])
style_card(ax3)
m_p = df.groupby(['MonthNum', 'Month'])['Profit'].sum().sort_index().reset_index()
bars3 = ax3.bar(m_p['Month'], m_p['Profit'], color=ORANGE_GLOW, width=0.45)
ax3.set_title('MONTHLY NET MARGIN PATTERNS', fontsize=12, fontweight='bold', pad=20, color=CYAN_GLOW, loc='left')
ax3.yaxis.grid(True, linestyle=':', alpha=0.15, color=TEXT_MAIN)
ax3.xaxis.grid(False)
ax3.set_ylim(0, m_p['Profit'].max() * 1.15)  # Vertical buffer room to shield labels from panel roof
ax3.bar_label(bars3, fmt='$%1.0f', padding=6, color=TEXT_MAIN, size=9, fontweight='bold')

# ---------------------------------------------------------
# ROW 3: REVENUE SEGMENTS
# ---------------------------------------------------------
# Chart 4: Top Products by Revenue
ax4 = fig.add_subplot(gs[2, 0:2])
style_card(ax4)
prod_s = df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(5).reset_index()
bars4 = ax4.bar(prod_s['Product'], prod_s['Sales'], color=[CYAN_GLOW, ORANGE_GLOW, PINK_GLOW, PURPLE_GLOW, YELLOW_GLOW], width=0.4)
ax4.set_title('TOP GROSS REVENUE SKUS RANKING', fontsize=12, fontweight='bold', pad=20, color=CYAN_GLOW, loc='left')
ax4.yaxis.grid(True, linestyle=':', alpha=0.15, color=TEXT_MAIN)
ax4.xaxis.grid(False)
ax4.set_ylim(0, prod_s['Sales'].max() * 1.15)
ax4.bar_label(bars4, fmt='$%1.0f', padding=6, color=TEXT_MAIN, fontweight='bold', size=10)

# Chart 5: Pricing Strategy Matrix (Donut - Outer Labels Decoupled)
ax5 = fig.add_subplot(gs[2, 2])
style_card(ax5)
df['Promo Band'] = df['Discount'].map(lambda x: 'Full Price' if x == 0 else ('Standard Promo' if x <= 0.1 else 'High Markdown'))
disc_q = df.groupby('Promo Band')['Quantity'].sum().reindex(['Full Price', 'Standard Promo', 'High Markdown']).dropna()
wedges5, texts5, autotexts5 = ax5.pie(
    disc_q, labels=None, autopct='%1.0f%%', pctdistance=0.75,
    colors=[CYAN_GLOW, PURPLE_GLOW, PINK_GLOW], startangle=140,
    textprops=dict(color=TEXT_MAIN, fontsize=11, fontweight='bold'), 
    wedgeprops=dict(width=0.45, edgecolor=BG_COLOR, linewidth=3)
)
ax5.legend(wedges5, disc_q.index, loc="lower center", bbox_to_anchor=(0.5, -0.15), ncol=3, frameon=False, fontsize=9)
ax5.set_title('VOLUME METRIC BY PRICING ELASTICITY', fontsize=12, fontweight='bold', pad=20, color=CYAN_GLOW)

# Chart 6: Profit Contribution by Unit SKU
ax6 = fig.add_subplot(gs[2, 3])
style_card(ax6)
prod_p = df.groupby('Product')['Profit'].sum().sort_values(ascending=True).reset_index()
bars6 = ax6.barh(prod_p['Product'], prod_p['Profit'], color=YELLOW_GLOW, height=0.45)
ax6.set_title('NET CONTROLLER HIGHLIGHT BY SKU', fontsize=12, fontweight='bold', pad=20, color=CYAN_GLOW, loc='left')
ax6.xaxis.grid(True, linestyle=':', alpha=0.15, color=TEXT_MAIN)
ax6.yaxis.grid(False)
ax6.set_xlim(0, prod_p['Profit'].max() * 1.25)
ax6.bar_label(bars6, fmt='$%1.0f', padding=12, color=TEXT_MAIN, size=10, fontweight='bold')

# Precise visual padding adjustment
plt.subplots_adjust(left=0.05, right=0.95, top=0.88, bottom=0.08)
plt.savefig('UltraClean_Executive_Dashboard.png', facecolor=BG_COLOR, dpi=300)
print("Ultra-clean high-contrast dashboard output saved!")
