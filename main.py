import os, asyncio
from nicegui import ui, app
import database, miner

# Configurări de Stil
ui.query('body').style('background-color: #0f172a; font-family: "Inter", sans-serif;')

# Variabile de stare
stats = {'leads': 0, 'status': 'SISTEM ACTIV'}

async def refresh_stats():
    # Aici vom număra mailurile din DB pe bune mai târziu
    pass

@ui.page('/')
async def main_page():
    # --- HEADER ---
    with ui.header().classes('items-center justify-between bg-slate-900 border-b border-slate-700 px-8 py-4'):
        with ui.row().classes('items-center gap-4'):
            ui.icon('auto_awesome', color='blue').classes('text-3xl')
            ui.label('MailAI SWARM OS').classes('text-2xl font-black text-white tracking-tighter')
        
        with ui.row().classes('items-center gap-6'):
            with ui.row().classes('items-center gap-2'):
                ui.badge('', color='emerald').classes('w-2 h-2 rounded-full animate-pulse')
                ui.label('DATABASE: ONLINE').classes('text-xs text-emerald-400 font-mono')
            ui.button(icon='settings', on_click=lambda: ui.notify('Setări')).flat().classes('text-slate-400')

    # --- SIDEBAR (DRAWER) ---
    with ui.left_drawer().classes('bg-slate-900 border-r border-slate-800 p-6').width(280):
        ui.label('CONTROL PANEL').classes('text-slate-500 text-xs font-bold mb-6 tracking-widest')
        
        with ui.column().classes('w-full gap-3'):
            ui.button('DASHBOARD', icon='dashboard').props('flat').classes('w-full justify-start text-blue-400 bg-blue-400/10 rounded-lg')
            ui.button('LEAD EXPLORER', icon='storage').props('flat').classes('w-full justify-start text-slate-400 hover:text-white')
            ui.button('SWARM MINER', icon='rocket_launch').props('flat').classes('w-full justify-start text-slate-400 hover:text-white')
            ui.button('EMAIL SENDER', icon='mail').props('flat').classes('w-full justify-start text-slate-400 hover:text-white')
        
        ui.separator().classes('my-8 bg-slate-800')
        
        with ui.column().classes('p-4 bg-slate-800/50 rounded-xl border border-slate-700'):
            ui.label('SUBSCRIPTION: PRO').classes('text-xs text-blue-400 font-bold')
            ui.linear_progress(value=0.3).classes('mt-2')
            ui.label('300k Leads Capacity').classes('text-[10px] text-slate-500 mt-1')

    # --- MAIN CONTENT ---
    with ui.column().classes('w-full max-w-6xl mx-auto p-8 gap-8'):
        
        # Stats Cards
        with ui.row().classes('w-full gap-6'):
            for label, value, icon, color in [
                ('TOTAL LEADS', '294,032', 'groups', 'blue'),
                ('MINING SPEED', '1.2k/hr', 'speed', 'emerald'),
                ('ACTIVE DRONES', '12', 'Vpn_key', 'amber'),
                ('BOUNCE RATE', '0.2%', 'error', 'rose')
            ]:
                with ui.card().classes(f'flex-1 bg-slate-800/40 border border-slate-700 p-6 rounded-2xl hover:border-{color}-500/50 transition-all'):
                    with ui.row().classes('justify-between items-center'):
                        ui.label(label).classes('text-slate-400 text-xs font-bold')
                        ui.icon(icon, color=color).classes('text-xl')
                    ui.label(value).classes('text-3xl font-bold text-white mt-2')

        # Chat & Terminal Section
        with ui.row().classes('w-full gap-8'):
            # Professional Chat Box
            with ui.column().classes('flex-[2] bg-slate-800/40 border border-slate-700 rounded-2xl overflow-hidden shadow-2xl'):
                ui.label('QUEEN ADVISOR').classes('bg-slate-800/80 px-6 py-3 text-sm font-bold text-slate-300 border-b border-slate-700 w-full')
                
                chat_container = ui.scroll_area().classes('w-full h-[450px] p-6 bg-slate-900/50')
                
                with ui.row().classes('w-full p-4 bg-slate-800/80 gap-2 border-t border-slate-700'):
                    input_field = ui.input(placeholder='Ordin pentru Regină...').props('borderless').classes('flex-1 text-white')
                    ui.button(icon='send', on_click=lambda: ui.notify('Se trimite...')).props('round flat').classes('text-blue-500')

            # Action Panel
            with ui.column().classes('flex-1 gap-4'):
                with ui.card().classes('w-full bg-gradient-to-br from-blue-600 to-indigo-700 p-6 rounded-2xl text-white shadow-lg shadow-blue-500/20'):
                    ui.label('PORNEȘTE MINERUL').classes('font-black text-lg')
                    ui.label('Lansează dronele pe nișa selectată.').classes('text-sm opacity-80 mb-4')
                    ui.button('EXECUTE SWARM', icon='bolt', on_click=lambda: miner.start_mining()).classes('bg-white text-blue-600 font-bold rounded-lg w-full py-4 shadow-xl')
                
                with ui.card().classes('w-full bg-slate-800/40 border border-slate-700 p-6 rounded-2xl'):
                    ui.label('TARGET NICHE').classes('text-slate-400 text-[10px] font-bold tracking-widest mb-4')
                    ui.select(['Real Estate', 'SaaS Tech', 'Dentists UK', 'Solar Energy'], value='SaaS Tech').classes('w-full')

# Pornire
ui.run(title='MailAI Swarm Elite', port=int(os.environ.get("PORT", 8080)), theme='dark')
