import customtkinter as ctk
import tkinter
from PIL import ImageTk, Image
import re

def create_window(title):
    ctk.set_default_color_theme("green")
    window = ctk.CTk()
    window.geometry("1400x800")
    ctk.set_appearance_mode("light")
    window.resizable(width=False, height=False)
    center_window(window)
    frame = create_frame(window)
    window.wm_title(title)
    return window, frame 

def center_window(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = 1400
    window_height = 800
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

def create_frame(window):
    frame = ctk.CTkFrame(master=window, width=750, height=600)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    return frame

def refresh_page(window, page_type):
    window.destroy()
    if page_type == "admin":
        admin_registration_page()
    elif page_type == "employee":
        employee_registration_page()
    else:
        login_page()

def login_page():
    Login_page_window, frame = create_window("Login Page")

    LogPg_ad_txt = ctk.CTkLabel(master=frame, text="Login as Admin:", font=('Roboto', 25))
    LogPg_ad_txt.place(x=85, y=50)

    LogPg_emp_txt = ctk.CTkLabel(master=frame, text="Login as Employee:", font=('Roboto', 25))
    LogPg_emp_txt.place(x=450, y=50)

    LogPg_accreg1_txt = ctk.CTkLabel(master=frame, font=('Roboto', 19), text="Don't have an account?   Register here as an")
    LogPg_accreg1_txt.place(x=15, y=565)
    
    LogPg_accreg2_txt = ctk.CTkLabel(master=frame, text="Or an", font=('Roboto', 18))
    LogPg_accreg2_txt.place(x=535, y=565)

    LogPg_ad_underline = ctk.CTkButton(master=frame, width=190, height=3, corner_radius=0, text="")
    LogPg_ad_underline.place(x=78, y=80)
 
    LogPg_emp_underline = ctk.CTkButton(master=frame, width=230, height=3, corner_radius=0, text="")
    LogPg_emp_underline.place(x=442, y=80)

    LogPG_ad_compnam_entry = ctk.CTkEntry(master=frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter Company Name...')
    LogPG_ad_compnam_entry.place(x=43, y=140)

    LogPG_ad_pass_entry = ctk.CTkEntry(master=frame, width=260, show="*", justify="center", font=('Roboto', 15), placeholder_text='Enter Password...')
    LogPG_ad_pass_entry.place(x=43, y=260)

    LogPg_emp_username_entry = ctk.CTkEntry(master=frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter Username...')
    LogPg_emp_username_entry.place(x=428, y=140)

    LogPg_emp_pass_entry = ctk.CTkEntry(master=frame, width=260, show="*", justify="center", font=('Roboto', 15), placeholder_text='Enter Password...')
    LogPg_emp_pass_entry.place(x=428, y=260)
    
    LogPg_emp_button = ctk.CTkButton(master=frame, width=200, text="Login", font=('Roboto', 15), corner_radius=20)
    LogPg_emp_button.place(x=75, y=350)

    LogPg_ad_button = ctk.CTkButton(master=frame, width=200, text="Login", font=('Roboto', 15), corner_radius=20)
    LogPg_ad_button.place(x=460, y=350)

    LogPg_settings_button = ctk.CTkButton(master=frame, width=100, corner_radius=20, text="Settings", font=('Roboto', 15))
    LogPg_settings_button.place(x=645, y=5)
    
    LogPg_refresh_button = ctk.CTkButton(master=frame, width=100, corner_radius=20, text="Refresh Page", font=('Roboto', 15))
    LogPg_refresh_button.place(x=5, y=5)
    LogPg_refresh_button.configure(command=lambda: refresh_page(Login_page_window, "login"))

    LogPg_emp_reg_button = ctk.CTkButton(master=frame, width=115, text="Employee", corner_radius=20, font=('Roboto', 15))
    LogPg_emp_reg_button.configure(command=lambda: refresh_page(Login_page_window, "employee"))
    LogPg_emp_reg_button.place(x=610, y=565)
    
    LogPg_ad_reg_button = ctk.CTkButton(master=frame, width=115, text="Admin", corner_radius=20, font=('Roboto', 15))
    LogPg_ad_reg_button.configure(command=lambda: refresh_page(Login_page_window, "admin"))
    LogPg_ad_reg_button.place(x=400, y=565)

    Login_page_window.mainloop()

def admin_registration_page():
    Admin_registration_window, admin_frame = create_window("Admin Registration")

    Adpg_ad_txt = ctk.CTkLabel(master=admin_frame, text="Admin Registration:", font=('Roboto', 25))
    Adpg_ad_txt.place(x=260, y=50)

    Adpg_ad_underline = ctk.CTkButton(master=admin_frame, width=230, height=3, corner_radius=0, text="")
    Adpg_ad_underline.place(x=250, y=80)

    Adpg_ad_firstname = ctk.CTkEntry(master=admin_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter First Name...')
    Adpg_ad_firstname.place(x=73, y=150)

    Adpg_ad_lastname = ctk.CTkEntry(master=admin_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter Last Name...')
    Adpg_ad_lastname.place(x=408, y=150)

    Adpg_ad_Password = ctk.CTkEntry(master=admin_frame, width=260, show="*", justify="center", font=('Roboto', 15), placeholder_text='Enter Password...')
    Adpg_ad_Password.place(x=73, y=315)

    Adpg_ad_ConfPassword = ctk.CTkEntry(master=admin_frame, width=260, show="*", justify="center", font=('Roboto', 15), placeholder_text='Confirm Password...')
    Adpg_ad_ConfPassword.place(x=408, y=315)

    Adpg_ad_compname = ctk.CTkEntry(master=admin_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter Company Name...')
    Adpg_ad_compname.place(x=238, y=430)

    Adpg_log_button = ctk.CTkButton(master=admin_frame, width=200, text="Register for an account", font=('Roboto', 18), corner_radius=20)
    
    AdPg_refresh_button = ctk.CTkButton(master=admin_frame, width=100, text="Refresh Page", font=('Roboto', 15), corner_radius=20)
    AdPg_refresh_button.place(x=5, y=5)
    AdPg_refresh_button.configure(command=lambda: refresh_page(Admin_registration_window, "admin"))
    
    AdPg_return_button = ctk.CTkButton(master=admin_frame, width=100, corner_radius=20, text="Return", font=('Roboto', 15))
    AdPg_return_button.configure(command=lambda: refresh_page(Admin_registration_window, "login"))
    AdPg_return_button.place(x=645, y=5)
    
    Admin_registration_window.mainloop()

def employee_registration_page():
    Employee_registration_window, employee_frame = create_window("Employee Registration")

    EmpReg_emp_txt = ctk.CTkLabel(master=employee_frame, text="Employee Registration:", font=('Roboto', 25))
    EmpReg_emp_txt.place(x=260, y=50)

    EmpReg_emp_underline = ctk.CTkButton(master=employee_frame, width=270, height=3, corner_radius=0, text="")
    EmpReg_emp_underline.place(x=253, y=80)

    EmpReg_emp_firstname = ctk.CTkEntry(master=employee_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter First Name...')
    EmpReg_emp_firstname.place(x=73, y=150)

    EmpReg_emp_lastname = ctk.CTkEntry(master=employee_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter Last Name...')
    EmpReg_emp_lastname.place(x=408, y=150)

    EmpReg_emp_password = ctk.CTkEntry(master=employee_frame, width=260, show="*", justify="center", font=('Roboto', 15), placeholder_text='Enter Password...')
    EmpReg_emp_password.place(x=73, y=295)

    EmpReg_emp_confpassword = ctk.CTkEntry(master=employee_frame, width=260, show="*", justify="center", font=('Roboto', 15), placeholder_text='Confirm Password...')
    EmpReg_emp_confpassword.place(x=408, y=295)

    EmpReg_emp_companyname = ctk.CTkEntry(master=employee_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter Company Name...')
    EmpReg_emp_companyname.place(x=73, y=430)

    EmpReg_emp_companyid = ctk.CTkEntry(master=employee_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter Company ID...')
    EmpReg_emp_companyid.place(x=408, y=430)

    EmpReg_log_button = ctk.CTkButton(master=employee_frame, width=200, text="Register for an account", font=('Roboto', 18), corner_radius=20)
    EmpReg_log_button.place(x=260, y=525)

    EmpReg_refresh_button = ctk.CTkButton(master=employee_frame, width=100, text="Refresh Page", font=('Roboto', 15), corner_radius=20)
    EmpReg_refresh_button.place(x=5, y=5)
    EmpReg_refresh_button.configure(command=lambda: refresh_page(Employee_registration_window, "employee"))
    
    EmpReg_return_button = ctk.CTkButton(master=employee_frame, width=100, corner_radius=20, text="Return", font=('Roboto', 15))
    EmpReg_return_button.configure(command=lambda: refresh_page(Employee_registration_window, "login"))
    EmpReg_return_button.place(x=645, y=5)
    
    Employee_registration_window.mainloop()

if __name__ == "__main__":
    login_page()
