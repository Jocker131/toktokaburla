


# LIMPEZA TOTAL: imports, app, funções, endpoints, bloco principal
import sqlite3
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
import logging
from flask import Flask, render_template, request, redirect, url_for
import threading
import pyautogui
from PIL import Image, ImageDraw, ImageFont
import time
import os

app = Flask(__name__)

# === CONFIGURAÇÃO IMEDIATA ===
PROXIES = [
    "189.1.2.3:8080",
    "201.2.3.4:3128",
]
MAIN_PROFILE_URL = "https://www.tiktok.com/@seu_perfil"
COMMENTS = ["Amei! 😍", "😂😂", "Top! 🔥"]

def setup_database():
    conn = sqlite3.connect('tiktok_engine.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS accounts (username TEXT, password TEXT, status TEXT DEFAULT 'active')''')
    c.execute('''CREATE TABLE IF NOT EXISTS engagement (video_url TEXT, likes INTEGER, comments INTEGER, timestamp REAL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS actions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        video_url TEXT,
        action_type TEXT,
        done INTEGER DEFAULT 0,
        timestamp REAL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS videos (url TEXT PRIMARY KEY, processed INTEGER DEFAULT 0)''')
    conn.commit()
    conn.close()

def add_account(username, password):
    conn = sqlite3.connect('tiktok_engine.db')
    c = conn.cursor()
    c.execute("INSERT INTO accounts (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

def generate_thumbnail(text, output_path="static/thumbnail.png"):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(base_dir, "static")
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)
    output_path_abs = os.path.join(static_dir, os.path.basename(output_path))
    img = Image.new('RGB', (1080, 1920), color=(30, 60, 114))
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        font = ImageFont.load_default()
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    position = ((1080 - text_width) // 2, (1920 - text_height) // 2)
    draw.text(position, text, font=font, fill=(255, 215, 0))
    img.save(output_path_abs)

def export_sqlite_to_csv():
    conn = sqlite3.connect('tiktok_engine.db')
    try:
        for table in ['accounts', 'engagement']:
            try:
                df = pd.read_sql_query(f'SELECT * FROM {table}', conn)
                df.to_csv(f'{table}.csv', index=False, encoding='utf-8-sig')
                print(f"Tabela {table} exportada para {table}.csv")
            except Exception as e:
                print(f"Erro ao exportar {table}: {e}")
    finally:
        conn.close()

# ...demais funções utilitárias e automação aqui...

@app.route('/')
def index():
    import datetime
    print('Acessando painel principal...')
    try:
        conn = sqlite3.connect('tiktok_engine.db')
        engagement_data = pd.read_sql_query("SELECT * FROM engagement ORDER BY timestamp DESC LIMIT 5", conn)
        accounts = pd.read_sql_query("SELECT username FROM accounts", conn)
        print('Dados carregados:', engagement_data.shape, accounts.shape)
        engagement_records = engagement_data.to_dict('records')
        for item in engagement_records:
            try:
                item['timestamp'] = datetime.datetime.fromtimestamp(int(item['timestamp'])).strftime('%d/%m/%Y %H:%M')
            except Exception:
                item['timestamp'] = ''
        conn.close()
        return render_template('index.html', status="Rodando", engagement_data=engagement_records, accounts=accounts.to_dict('records'))
    except Exception as e:
        print('Erro ao carregar dados para o painel:', e)
        return render_template('index.html', status=f"Erro: {e}", engagement_data=[], accounts=[])

@app.route('/add_account', methods=['POST'])
def add_account_route():
    username = request.form['username']
    password = request.form['password']
    add_account(username, password)
    return "Conta adicionada!"

# ...demais endpoints Flask...

if __name__ == '__main__':
    setup_database()
    add_account("conta1@gmail.com", "TikTok2025!")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(base_dir, "static")
    thumbnail_path = os.path.join(static_dir, "thumbnail.png")
    if not os.path.exists(thumbnail_path):
        generate_thumbnail("TikTok Viral Engine")
    export_sqlite_to_csv()
    app.run(host='127.0.0.1', port=5000)
# Bloco principal no final
if __name__ == '__main__':
    setup_database()
    add_account("conta1@gmail.com", "TikTok2025!")
    # Garante que o thumbnail exista no caminho correto
    base_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(base_dir, "static")
    thumbnail_path = os.path.join(static_dir, "thumbnail.png")
    if not os.path.exists(thumbnail_path):
        generate_thumbnail("TikTok Viral Engine")
    # Exporta automaticamente as tabelas do banco para CSV
    export_sqlite_to_csv()
    app.run(host='127.0.0.1', port=5000)

import sqlite3
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
import logging
from flask import Flask, render_template, request, redirect, url_for
import threading
import pyautogui
from PIL import Image, ImageDraw, ImageFont
import time

# Configurar logs
logging.basicConfig(filename='tiktok_engine.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Flask
app = Flask(__name__)


# === CONFIGURAÇÃO IMEDIATA ===
# Edite abaixo com seus proxies reais (exemplo: "189.1.2.3:8080")
PROXIES = [
    "189.1.2.3:8080",  # Exemplo
    "201.2.3.4:3128",  # Exemplo
    # Adicione mais proxies reais aqui
]

# Edite aqui o perfil principal do TikTok (exemplo: https://www.tiktok.com/@seu_perfil)
MAIN_PROFILE_URL = "https://www.tiktok.com/@seu_perfil"


# Comentários
COMMENTS = ["Amei! 😍", "😂😂", "Top! 🔥"]


# Banco de dados
def setup_database():
    conn = sqlite3.connect('tiktok_engine.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS accounts (username TEXT, password TEXT, status TEXT DEFAULT 'active')''')
    c.execute('''CREATE TABLE IF NOT EXISTS engagement (video_url TEXT, likes INTEGER, comments INTEGER, timestamp REAL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS actions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        video_url TEXT,
        action_type TEXT,
        done INTEGER DEFAULT 0,
        timestamp REAL
    )''')
    conn.commit()
    conn.close()

# Função para criar contas fake (simulação)
def create_fake_account():
    import string
    username = 'user_' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + '@gmail.com'
    password = 'TikTok' + ''.join(random.choices(string.digits, k=4)) + '!'
    add_account(username, password)
    return username, password

# Garante o mínimo de contas seguindo o perfil
def ensure_minimum_accounts(main_profile, min_count=25):
    conn = sqlite3.connect('tiktok_engine.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM accounts WHERE status='active'")
    count = c.fetchone()[0]
    to_create = max(0, min_count - count)
    created = []
    for _ in range(to_create):
        username, password = create_fake_account()
        created.append(username)
    conn.close()
    return created

# Marca ação feita
def mark_action(username, video_url, action_type):
    conn = sqlite3.connect('tiktok_engine.db')
    c = conn.cursor()
    c.execute("INSERT INTO actions (username, video_url, action_type, done, timestamp) VALUES (?, ?, ?, 1, ?)" ,
              (username, video_url, action_type, time.time()))
    conn.commit()
    conn.close()

# Verifica se ação já foi feita
def has_done_action(username, video_url, action_type):
    conn = sqlite3.connect('tiktok_engine.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM actions WHERE username=? AND video_url=? AND action_type=? AND done=1", (username, video_url, action_type))
    done = c.fetchone()[0] > 0
    conn.close()
    return done

# Adicionar conta
def add_account(username, password):
    conn = sqlite3.connect('tiktok_engine.db')
    c = conn.cursor()
    c.execute("INSERT INTO accounts (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

# Gerar thumbnail
def generate_thumbnail(text, output_path="static/thumbnail.png"):
    import os
    # Caminho absoluto para a pasta static
    base_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(base_dir, "static")
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)
    output_path_abs = os.path.join(static_dir, os.path.basename(output_path))
    img = Image.new('RGB', (1080, 1920), color=(30, 60, 114))
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        font = ImageFont.load_default()
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    position = ((1080 - text_width) // 2, (1920 - text_height) // 2)
    draw.text(position, text, font=font, fill=(255, 215, 0))
    img.save(output_path_abs)

# Configurar navegador
def setup_browser():
    options = Options()
    options.add_argument("--headless")
    if PROXIES:
        options.add_argument(f'--proxy-server={random.choice(PROXIES)}')
    driver = webdriver.Chrome(options=options)
    return driver

# Automação
def automate_tiktok(profile_url, username, password, video_url=None):
    driver = setup_browser()
    driver.get("https://www.tiktok.com/login")
    sleep(random.uniform(2, 4))

    try:
        pyautogui.click(x=100, y=100)
        driver.find_element(By.ID, "login-button").click()
        sleep(1)
        pyautogui.typewrite(username)
        pyautogui.press('tab')
        pyautogui.typewrite(password)
        pyautogui.press('enter')
        sleep(random.uniform(4, 6))
    except Exception as e:
        logging.error(f"Erro no login: {e}")
        driver.quit()
        return

    target_url = video_url if video_url else profile_url
    driver.get(target_url)
    sleep(random.uniform(2, 4))

    engagement_data = {'video_url': target_url, 'likes': 0, 'comments': 0, 'timestamp': time.time()}
    videos = driver.find_elements(By.CLASS_NAME, "video-feed-item")[:3] if not video_url else [driver]
    for video in videos:
        try:
            if not video_url:
                pyautogui.click(video.location['x'] + 50, video.location['y'] + 50)
            sleep(random.uniform(8, 12))
            like_button = driver.find_element(By.CLASS_NAME, "like-button")
            if "liked" not in like_button.get_attribute("class"):
                pyautogui.click(like_button.location['x'], like_button.location['y'])
                engagement_data['likes'] += 1
            sleep(random.uniform(1, 2))
            comment_input = driver.find_element(By.CLASS_NAME, "comment-input")
            comment = random.choice(COMMENTS)
            pyautogui.typewrite(comment)
            pyautogui.press('enter')
            engagement_data['comments'] += 1
            sleep(random.uniform(1, 2))
        except:
            continue

    conn = sqlite3.connect('tiktok_engine.db')
    pd.DataFrame([engagement_data]).to_sql('engagement', conn, if_exists='append', index=False)
    conn.close()
    driver.quit()

# Rotação de contas

def run_automation(profile_url, video_url=None, min_accounts=25):
    # Garante o mínimo de contas
    ensure_minimum_accounts(profile_url, min_accounts)
    conn = sqlite3.connect('tiktok_engine.db')
    accounts = pd.read_sql_query("SELECT * FROM accounts WHERE status='active'", conn)
    conn.close()
    # Simula pegar todos os vídeos do perfil (exemplo)
    videos = [video_url] if video_url else [profile_url + '/video1', profile_url + '/video2', profile_url + '/video3']
    elogios = ["Muito bom!", "Parabéns pelo vídeo!", "Conteúdo top!", "Show demais!", "Mandou bem!", "Amei esse vídeo!"]
    for _, account in accounts.iterrows():
        username = account['username']
        password = account['password']
        # Seguir perfil principal (simulação)
        if not has_done_action(username, profile_url, 'follow'):
            print(f"{username} seguindo {profile_url}")
            mark_action(username, profile_url, 'follow')
        for video in videos:
            # Curtir vídeo
            if not has_done_action(username, video, 'like'):
                print(f"{username} curtindo {video}")
                mark_action(username, video, 'like')
            # Comentar 3 vezes
            for i in range(3):
                if not has_done_action(username, video, f'comment_{i}'):
                    elogio = random.choice(elogios)
                    print(f"{username} comentando no {video}: {elogio}")
                    mark_action(username, video, f'comment_{i}')
            # Copiar link
            if not has_done_action(username, video, 'copy_link'):
                print(f"{username} copiou o link de {video}")
                mark_action(username, video, 'copy_link')
        sleep(random.uniform(2, 4))

# Flask
app = Flask(__name__)

@app.route('/')
def index():
    import datetime
    print('Acessando painel principal...')
    try:
        conn = sqlite3.connect('tiktok_engine.db')
        engagement_data = pd.read_sql_query("SELECT * FROM engagement ORDER BY timestamp DESC LIMIT 5", conn)
        accounts = pd.read_sql_query("SELECT username FROM accounts", conn)
        print('Dados carregados:', engagement_data.shape, accounts.shape)
        # Formatar o timestamp para string legível
        engagement_records = engagement_data.to_dict('records')
        for item in engagement_records:
            try:
                item['timestamp'] = datetime.datetime.fromtimestamp(int(item['timestamp'])).strftime('%d/%m/%Y %H:%M')
            except Exception:
                item['timestamp'] = ''
        conn.close()
        return render_template('index.html', status="Rodando", engagement_data=engagement_records, accounts=accounts.to_dict('records'))
    except Exception as e:
        print('Erro ao carregar dados para o painel:', e)
        return render_template('index.html', status=f"Erro: {e}", engagement_data=[], accounts=[])

@app.route('/start', methods=['POST', 'GET'])
def start_automation():
    if request.method == 'POST':
        profile_url = request.form['profile_url']
        video_url = request.form.get('video_url', '')
    else:
        profile_url = request.args.get('profile_url')
        video_url = request.args.get('video_url', '')
    threading.Thread(target=run_automation, args=(profile_url, video_url)).start()
    generate_thumbnail(f"Viral: {profile_url}")
    if request.method == 'POST':
        return redirect(url_for('index'))
    else:
        return {"status": "automação iniciada", "profile_url": profile_url, "video_url": video_url}

@app.route('/add_account', methods=['POST'])
def add_account_route():
    username = request.form['username']
    password = request.form['password']
    add_account(username, password)
    return "Conta adicionada!"

import os

if __name__ == '__main__':
    setup_database()
    add_account("conta1@gmail.com", "TikTok2025!")
    # Garante que o thumbnail exista no caminho correto
    base_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(base_dir, "static")
    thumbnail_path = os.path.join(static_dir, "thumbnail.png")
    if not os.path.exists(thumbnail_path):
        generate_thumbnail("TikTok Viral Engine")
    # Exporta automaticamente as tabelas do banco para CSV
    export_sqlite_to_csv()
    app.run(host='127.0.0.1', port=5000)
