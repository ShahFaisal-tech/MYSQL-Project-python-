from tkinter import *
from tkinter import messagebox
from Admin_Add_page import Add_Student_screen
from Delete import Delete_Window
from Search_Student import Search_Screen
from update import Update_Screen
from connectdb import *
print(conn)


class Admin_Dashboard_Screen:
    def __init__(self,root,admin_screen):
        self.root=root
        self.admin_screen=admin_screen
        self.root.overrideredirect(True)
        self.root.title("Admin Dashboard Page")
        self.root.state("zoomed")
        self.root.resizable(width=False, height=False)
        self.root.config(bg="#E0F7FA")

        self.root.rowconfigure(1, weight=0)

        left_frame=Frame(self.root,bg="#1E293B")
        left_frame.grid(row=0, column=0,rowspan=30,columnspan=2,sticky="nsew")

        for i in range(10):
            self.root.columnconfigure(i, weight=1)

        self.root.rowconfigure(0, weight=0)
        self.root.rowconfigure(1, weight=1)

        header = Frame(self.root, bg="#1a73e8", height=60)
        header.grid(row=0, column=0, columnspan=10, sticky="nsew")

        Label(header,
              text="MMANTC Admin Dashboard",
              font=("Century", 22, "bold"),
              bg="#1a73e8",
              fg="white").pack(expand=True)

        admin_btn=Button(self.root,text="Add Student",font=("Roboto",15,"bold"),width=20,bg="Skyblue",command=self.open_add_student)
        admin_btn.grid(row=1,column=0,columnspan=2,padx=5,pady=20,sticky=W)
        delete_stud_btn = Button(self.root,text="Delete Student",font=("Roboto",15,"bold"),width=20,bg="Skyblue",command=self.open_delete_student)
        delete_stud_btn.grid(row=2, column=0,columnspan=2,padx=5,pady=20,sticky="wn")
        update_stud_btn = Button(self.root, text="Update Student", font=("Roboto", 15, "bold"), width=20, bg="Skyblue",command=self.open_update_student)
        update_stud_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=20,sticky="wn")
        search_stud_btn = Button(self.root, text="Search Student", font=("Roboto", 15, "bold"), width=20, bg="Skyblue",command=self.open_search_student)
        search_stud_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=20,sticky="wn")
        exit_btn = Button(self.root,text="Exit",font=("Roboto", 15, "bold"),command=self.exit_fun,width=20, bg="#FF2E2E")
        exit_btn.grid(row=5, column=0, columnspan=2, padx=5, pady=20,sticky="wn")
        logout_btn = Button(self.root, text="Logout", font=("Roboto", 15, "bold"), command=self.logout, width=20,bg="RoyalBlue1")
        logout_btn.grid(row=6, column=0, columnspan=2, padx=5, pady=20, sticky="wn")


        box_width = 20
        box_height = 4

        l_students = Label(self.root,
                           text="Total Students\n955",
                           font=("Roboto", 16, "bold"),
                           width=box_width,
                           height=box_height,
                           bg="#E3F2FD",
                           relief="ridge")
        l_students.grid(row=2, column=3, padx=20, pady=15)

        student_male = Label(self.root,
                             text="Total Male Students\n550",
                             font=("Roboto", 16, "bold"),
                             width=box_width,
                             height=box_height,
                             bg="#E8F5E9",
                             relief="ridge")
        student_male.grid(row=2, column=4, padx=20, pady=15)

        student_female = Label(self.root,
                               text="Total Female Students\n405",
                               font=("Roboto", 16, "bold"),
                               width=box_width,
                               height=box_height,
                               bg="#F3E5F5",
                               relief="ridge")
        student_female.grid(row=2, column=5, padx=20, pady=15)

        diploma_student = Label(self.root,
                               text="Total Diploma Students\n405",
                               font=("Roboto", 16, "bold"),
                               width=box_width,
                               height=box_height,
                               bg="#FFF3E0",
                                relief="ridge")
        diploma_student.grid(row=3, column=3, padx=20, pady=15)

        Degree_student = Label(self.root,
                                text="Total Degree Students\n550",
                                font=("Roboto", 16, "bold"),
                                width=box_width,
                                height=box_height,
                                bg="#ECEFF1",
                                relief="ridge")
        Degree_student.grid(row=3, column=4, padx=20, pady=15)

        Total_Faculty = Label(self.root,
                               text="Total Faculty\n56",
                               font=("Roboto", 16, "bold"),
                               width=box_width,
                               height=box_height,
                               bg="#FFE5D9",
                               relief="ridge")
        Total_Faculty.grid(row=3, column=5, padx=20, pady=15)


    def exit_fun(self):
        ask=messagebox.askyesno("Exit","Are you sure you want to exit?")
        if ask:
            self.root.destroy()
        else:
            pass

    def logout(self):
        a = messagebox.askyesno("Logout", "Are you sure you want to Logout?")
        if a:
            self.root.destroy()  # close dashboard
            self.admin_screen.deiconify()  # show login again
            messagebox.showinfo("Logout", "Logged out successfully!")

    def open_add_student(self):
        self.root.withdraw()
        new_window = Toplevel()
        Add_Student_screen(new_window, self.root)

    def open_delete_student(self):
        self.root.withdraw()
        new_window = Toplevel()
        Delete_Window(new_window, self.root)

    def open_search_student(self):
        self.root.withdraw()
        new_window = Toplevel()
        Search_Screen(new_window, self.root)

    def open_update_student(self):
        self.root.withdraw()
        new_window = Toplevel()
        Update_Screen(new_window, self.root)

# from tkinter import *
# from tkinter import messagebox

# class Admin_Dashboard_Screen:
#     def __init__(self, root, admin_screen):
#         self.root = root
#         self.admin_screen = admin_screen
#
#         self.root.title("Admin Dashboard")
#         self.root.geometry("1366x768")
#         self.root.configure(bg="#f4f6f9")
#         self.root.resizable(False, False)
#
#         self.root.columnconfigure(0, weight=1)  # Sidebar
#         self.root.columnconfigure(1, weight=4)  # Main Content
#         self.root.rowconfigure(1, weight=1)
#
#         header = Frame(self.root, bg="#1a73e8", height=60)
#         header.grid(row=0, column=0, columnspan=2, sticky="nsew")
#
#         header.columnconfigure(0, weight=1)
#
#         Label(header,
#               text="MMANTC Admin Dashboard",
#               font=("Century", 20, "bold"),
#               bg="#1a73e8",
#               fg="white").grid(row=0, column=0, padx=20, pady=10, sticky=W)
#
#         Button(header,
#                text="Logout",
#                font=("Roboto", 10, "bold"),
#                bg="red",
#                fg="white",
#                command=self.logout).grid(row=0, column=1, padx=20)
#
#         sidebar = Frame(self.root, bg="#263238", width=250)
#         sidebar.grid(row=1, column=0, sticky="nsew")
#
#         sidebar.rowconfigure(6, weight=1)
#
#         menu_buttons = [
#             ("Add Student", None),
#             ("Delete Student", None),
#             ("Update Student", None),
#             ("Search Student", None),
#             ("Exit", self.exit_fun)
#         ]
#
#         for i, (text, cmd) in enumerate(menu_buttons):
#             Button(sidebar,
#                    text=text,
#                    font=("Roboto", 12, "bold"),
#                    bg="#37474F",
#                    fg="white",
#                    width=20,
#                    relief=FLAT,
#                    command=cmd).grid(row=i, column=0, padx=20, pady=15, sticky="w")
#
#         self.content = Frame(self.root, bg="white")
#         self.content.grid(row=1, column=1, sticky="nsew")
#
#         Label(self.content,
#               text="Welcome Admin!",
#               font=("Century", 18, "bold"),
#               bg="white").grid(row=0, column=0, padx=30, pady=30)
#
#
#     def exit_fun(self):
#         ask = messagebox.askyesno("Exit", "Are you sure you want to exit?")
#         if ask:
#             self.root.destroy()
#
#     def logout(self):
#         a = messagebox.askyesno("Logout", "Are you sure you want to Logout?")
#         if a:
#             self.root.destroy()
#             self.admin_screen.deiconify()
# from tkinter import *
# from tkinter import messagebox
#
# class Admin_Dashboard_Screen:
#     def __init__(self, root, admin_screen):
#         self.root = root
#         self.admin_screen = admin_screen
#
#         # Fullscreen by default
#         self.root.state("zoomed")   # For Windows
#         # self.root.attributes("-fullscreen", True)  # Use this for Mac/Linux
#
#         self.root.title("Admin Dashboard Page")
#         self.root.configure(bg="white")
#
#         # ================= HEADER =================
#         header = Label(self.root,
#                        text="MMANTC Admin Dashboard",
#                        font=("Century", 25, "bold"),
#                        bg="white",
#                        fg="#1E3A8A")
#         header.pack(pady=20)
#
#         # ================= SIDEBAR =================
#         sidebar = Frame(self.root, bg="#1E293B", width=250)
#         sidebar.pack(side=LEFT, fill=Y)
#
#         # Sidebar Title
#         Label(sidebar,
#               text="MENU",
#               font=("Century", 18, "bold"),
#               bg="#1E293B",
#               fg="white").pack(pady=20)
#
#         # Button Style
#         btn_style = {
#             "font": ("Roboto", 14, "bold"),
#             "width": 20,
#             "bg": "#334155",
#             "fg": "white",
#             "bd": 0,
#             "activebackground": "#475569",
#             "activeforeground": "white",
#             "pady": 10
#         }
#
#         Button(sidebar, text="Add Student", **btn_style).pack(pady=10)
#         Button(sidebar, text="Delete Student", **btn_style).pack(pady=10)
#         Button(sidebar, text="Update Student", **btn_style).pack(pady=10)
#         Button(sidebar, text="Search Student", **btn_style).pack(pady=10)
#
#         Button(sidebar, text="Logout",
#                command=self.logout,
#                bg="#DC2626",
#                fg="white",
#                font=("Roboto", 12, "bold"),
#                width=20).pack(pady=20)
#
#         Button(sidebar, text="Exit",
#                command=self.exit_fun,
#                bg="#B91C1C",
#                fg="white",
#                font=("Roboto", 12, "bold"),
#                width=20).pack(pady=10)
#
#         # ================= MAIN AREA =================
#         main_area = Frame(self.root, bg="white")
#         main_area.pack(side=LEFT, fill=BOTH, expand=True)
#
#
#     def exit_fun(self):
#         ask = messagebox.askyesno("Exit", "Are you sure you want to exit?")
#         if ask:
#             self.root.destroy()
#
#     def logout(self):
#         a = messagebox.askyesno("Logout", "Are you sure you want to Logout?")
#         if a:
#             self.root.withdraw()
#             self.admin_screen.deiconify()
