import tkinter
from tkinter import messagebox
import threading
import time
import platform

OS_TYPE = platform.system()

# 색깔, 폰트 설정
INPUT_PANEL_BG = "#242932"
INPUT_PANEL_TEXT = "#F4F5FC"
MAP_FRAME_BG = "#FFFFFF"
TITLE_FONT = "나눔고딕 12 bold"
TEXT_FONT = "나눔고딕 10"
BUTTON_TEXT_FONT = "나눔고딕 8"

# 기본 윈도우 설정
window=tkinter.Tk()
window.title("Nurinarae WCRC mission planner")
window.geometry("1366x768+50+25")
window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
if OS_TYPE == 'Darwin':
    input_panel_width = int(window_width * 0.3)
else:
    input_panel_width = int(window_width * 0.25)
map_frame_width = window_width - input_panel_width
input_panel_height = window_height
map_frame_height = window_height

# 커맨드 입력 부분
input_panel=tkinter.Canvas(window, relief="flat", bd=2, bg=INPUT_PANEL_BG, width=input_panel_width, height= input_panel_height, borderwidth=0, highlightthickness=0, scrollregion=(0,0,0,5500))

input_panel.grid(row=0, column=0)
place_title = input_panel.create_text(20, 30, text="미션 설정", font=TITLE_FONT, fill=INPUT_PANEL_TEXT , width=input_panel_width, anchor=tkinter.W)
num_of_mission = input_panel.create_text(20, 52, text= "미션의 수:", font=TEXT_FONT, fill=INPUT_PANEL_TEXT, width=input_panel_width, anchor=tkinter.W)
mission_num_entry = tkinter.Entry(window)
input_panel.create_window(120,52,window=mission_num_entry, anchor=tkinter.W)
task_created_flag = False

def missionconfirm():
    for entry in missionstartentry:
        print(entry.get())

# 행선지 입력부분
missionstartentry = []
missionendentry = [] 
create_task_final_y = 77
def create_task():
    global task_created_flag, missionentry, create_task_final_y
    missionstartlabel = []
    missionendlabel = []
    if not task_created_flag:
        task_created_flag = True
        mission_num_button.config(text="지우기")
        num = int(mission_num_entry.get())
        text_x = 20
        
        entry_x = 120
        
        if OS_TYPE == 'Darwin':
            widget_gap = 80
            text_y = 90
            entry_y = 90
        else:
            widget_gap = 50
            text_y = 77
            entry_y = 77
        for i in range(0,num):
            missionstartlabel.append(i)
            entrybox_start = tkinter.Entry(window)
            entrybox_end = tkinter.Entry(window)
            missionstartentry.append(entrybox_start)
            missionendlabel.append(i)
            missionendentry.append(entrybox_end)
            missionstartlabel[i] = input_panel.create_text(text_x, text_y + (widget_gap*i), text = "미션 "+str(i+1)+" 시작지점:", font=TEXT_FONT, fill=INPUT_PANEL_TEXT, width=input_panel_width, tags="auto-gen", anchor=tkinter.W)
            input_panel.create_window(entry_x, entry_y+(widget_gap*i), window=missionstartentry[i], tags="auto-gen" ,anchor=tkinter.W)
            missionendlabel[i] = input_panel.create_text(text_x, text_y + (widget_gap*i)+(widget_gap/2-10), text="미션 "+str(i+1)+" 종료지점:",font=TEXT_FONT, fill=INPUT_PANEL_TEXT, width=input_panel_width, tags="auto-gen", anchor=tkinter.W)
            input_panel.create_window(entry_x, entry_y+ (widget_gap*i)+(widget_gap/2-10), window=missionendentry[i], tags="auto-gen", anchor=tkinter.W)
        confirm_button = tkinter.Button(window, text="확인", font=BUTTON_TEXT_FONT, command=missionconfirm, bd = 0)
        create_task_final_y = text_y+(widget_gap*i)+widget_gap
        input_panel.create_window(text_x,create_task_final_y , window=confirm_button, anchor=tkinter.W, tags="auto-gen")
    elif task_created_flag:
        input_panel.delete("auto-gen")
        missionentry = []
        mission_num_button.config(text="확인")
        create_task_final_y = 77
        task_created_flag = False

mission_num_button = tkinter.Button(window, text="확인", font=BUTTON_TEXT_FONT, command= create_task, bd=0)
if OS_TYPE == 'Darwin':
    input_panel.create_window(320,52,window=mission_num_button, anchor=tkinter.W)   
else: 
    input_panel.create_window(280,52,window=mission_num_button, anchor=tkinter.W)

# 장애물 입력부분
obstacle_title = input_panel.create_text(20, create_task_final_y + 50, text="장애물 설정", font=TITLE_FONT, fill=INPUT_PANEL_TEXT , width=input_panel_width, anchor=tkinter.W)
num_of_obstacle = input_panel.create_text(20, create_task_final_y + 50 + 38, text= "장애물의 수:", font=TEXT_FONT, fill=INPUT_PANEL_TEXT, width=input_panel_width, anchor=tkinter.W)
obstacle_num_entry = tkinter.Entry(window)
canvas_obstacle_num_entry = input_panel.create_window(120,create_task_final_y + 50 + 38,window=obstacle_num_entry, anchor=tkinter.W)
obstacle_created_flag = False
def obstacleconfirm():
    for entry in obstacleentry:
        print(entry.get())
obstacleentry = []
create_obstacle_final_y = create_task_final_y+88

def create_task_obstacle():
    global obstacle_created_flag, obstacleentry, create_obstacle_final_y
    obstaclelabel = []
    if not obstacle_created_flag:
        obstacle_created_flag = True
        obstacle_num_button.config(text="지우기")
        num = int(obstacle_num_entry.get())
        text_x = 20
        
        entry_x = 120
        
        if OS_TYPE == 'Darwin':
            widget_gap = 40
            text_y = create_obstacle_final_y+38
            entry_y = create_obstacle_final_y+38
        else:
            widget_gap = 50
            text_y = create_obstacle_final_y+25
            entry_y = create_obstacle_final_y+25
        for i in range(0,num):
            obstaclelabel.append(i)
            entrybox = tkinter.Entry(window)
            obstacleentry.append(entrybox)
            obstaclelabel.append(i)
            obstaclelabel[i] = input_panel.create_text(text_x, text_y + (widget_gap*i), text = "장애물 "+str(i+1)+" 위치:", font=TEXT_FONT, fill=INPUT_PANEL_TEXT, width=input_panel_width, tags="auto-gen-o", anchor=tkinter.W)
            input_panel.create_window(entry_x, entry_y+(widget_gap*i), window=obstacleentry[i], tags="auto-gen-o" ,anchor=tkinter.W)
        confirm_button = tkinter.Button(window, text="확인", font=BUTTON_TEXT_FONT, command=obstacleconfirm, bd = 0)
        create_obstacle_final_y = text_y+(widget_gap*i)+widget_gap
        input_panel.create_window(text_x,create_obstacle_final_y , window=confirm_button, anchor=tkinter.W, tags="auto-gen-o")
    elif obstacle_created_flag:
        input_panel.delete("auto-gen-o")
        obstacleentry = []
        obstacle_num_button.config(text="확인")
        create_obstacle_final_y = create_task_final_y+88
        obstacle_created_flag = False
obstacle_num_button = tkinter.Button(window, text="확인", font=BUTTON_TEXT_FONT, command= create_task_obstacle, bd=0)
if OS_TYPE == 'Darwin':
    input_panel.create_window(320,create_task_final_y+88,window=obstacle_num_button, anchor=tkinter.W)   
else: 
    input_panel.create_window(280,create_task_final_y+88,window=obstacle_num_button, anchor=tkinter.W)

# 스크롤바
vbar=tkinter.Scrollbar(window,orient=tkinter.VERTICAL)
vbar.grid(row=0, column=1, sticky=tkinter.NS)
vbar.config(command=input_panel.yview)
input_panel.config(yscrollcommand=vbar.set)

# 맵 입력 부분
map_frame=tkinter.Canvas(window, relief="flat", bd=2, bg=MAP_FRAME_BG, width=input_panel_width, height= input_panel_height, borderwidth=0, highlightthickness=0)
map_frame.grid(row=0, column=2)

# 해상도 변화 대응하는 부분
end_flag = False
def dynamic_size():
    global end_flag, end_job_flag
    global input_panel_height,input_panel_width
    global map_frame_height, map_frame_width
    while not end_flag:
        window.update_idletasks()
        window_width = window.winfo_width()
        window_height = window.winfo_height()

        if OS_TYPE == 'Darwin':
            input_panel_width = int(window_width * 0.3)
        else:
            input_panel_width = int(window_width * 0.25)
        map_frame_width = window_width - input_panel_width

        input_panel_height = window_height
        map_frame_height = window_height

        input_panel.config(width=input_panel_width, height= input_panel_height)
        map_frame.config(width=map_frame_width, height=map_frame_height)
        input_panel.configure(scrollregion=(0,0,0,create_task_final_y*2))
        input_panel.coords(obstacle_title, 20, create_task_final_y+50)
        input_panel.coords(num_of_obstacle, 20, create_task_final_y+50+38)
        input_panel.coords(canvas_obstacle_num_entry, 120, create_task_final_y+50+38)
        input_panel.coords(obstacle_num_button, 320, create_task_final_y+50+38)
        
        time.sleep(0.1)

# 종료 팝업
def on_closing():
    global end_flag
    if messagebox.askokcancel("다시 한번 물어보겠습니다...", "정말 종료하려는겁니까 휴먼?"):
        end_flag = True
        if OS_TYPE == 'Windows':
            window.destroy()
        elif OS_TYPE == 'Darwin':
            window.quit()

window.protocol("WM_DELETE_WINDOW", on_closing)

dynamic_size_thread = threading.Thread(target=dynamic_size)
dynamic_size_thread.start()
window.mainloop()
