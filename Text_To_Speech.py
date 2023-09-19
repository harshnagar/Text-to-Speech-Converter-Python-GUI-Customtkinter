from customtkinter import *
import pyttsx3
from PIL import ImageTk, Image
import webbrowser


def main_win():
    main = CTk()
    main.title("TGZ Text To Speech Converter")
    main.geometry("400x400+420+100")
    main.resizable(0, 0)
    main.iconbitmap("TGZ_icon.ico")
    voice_dt = StringVar()
    voice_speed_var = IntVar()
    voice_speed_var.set(110)
    voice_dt.set("Male")
    TGZ_symb = CTkImage(dark_image=Image.open("TGZ Icon.png"), size=(40, 40))
    engine = pyttsx3.init()

    def notify(notification):
        def close_noti():
            noti_frame.destroy()
            noti_frame.grab_release()

        noti_frame = CTkFrame(main, fg_color='grey10', corner_radius=10, bg_color='grey20')
        noti_frame.grab_set()
        noti_frame.grid(row=2, column=0, sticky="nw", padx=80, pady=80)
        noti_head = CTkLabel(noti_frame, text="Notification", fg_color='red', corner_radius=10, height=10, width=10,bg_color='grey20')
        noti_head.grid(row=0, column=0, sticky="nswe")
        noti_text = CTkLabel(noti_frame, text=notification, fg_color='grey10', wraplength=270)
        noti_text.grid(row=1, column=0, sticky="w", padx=5,pady=5)
        ok_btn = CTkButton(noti_frame, command=close_noti, text='OK', fg_color='green2', cursor="hand2", text_color="black",
                           width=20, height=20)
        ok_btn.grid(row=2, column=0, sticky="e", padx=5, pady=5)

    def convert():
        text = entry_box.get("1.0", 'end-1c')
        if len(text) == 0:
            msg = "Please Write Something in the Text Box in order to Convert it to Audio!"
            notify(msg)
        else:
            save_dir = filedialog.asksaveasfilename(filetypes=[('.mp3', "")], initialfile="Audio")
            if save_dir == "":
                pass
            else:
                print(voice_speed_var.get())
                print(voice_dt.get())
                print(text)
                engine.setProperty('rate', voice_speed_var.get())
                voices = engine.getProperty('voices')
                if voice_dt.get() == 'Male':
                    engine.setProperty('voice', voices[0].id)
                else:
                    engine.setProperty('voice', voices[1].id)
                try:
                    main.config(cursor="wait")
                    engine.save_to_file(text, save_dir+'.mp3')
                except Exception as e:
                    main.config(cursor="")
                    print(str(e))
                    notify("Please refer the Error to Admin: "+str(e))

                main.config(cursor="")
                engine.runAndWait()
                notify("Text Successfully Converted to Audio! ")

    def open_github():
        webbrowser.open_new_tab("https://github.com/harshnagar")

    def om_callback(choice):
        voice_dt.set(choice)

    TGZ_symb_lab = CTkButton(main, font=("Helvita", 15, "bold"), command=open_github, height=40, width=400, image=TGZ_symb,
                           cursor="hand2", text="Text To Speech Converter", fg_color="black", compound="left")
    TGZ_symb_lab.grid(row=0, column=0, sticky="w")

    voice_text = CTkLabel(main, text="Voice Type", width=100)
    voice_text.grid(row=1, column=0, sticky='w', padx=0, pady=5)
    voice_opt = CTkOptionMenu(main, width=100, values=["Male", "Female"], command=om_callback, fg_color="grey20")
    voice_opt.grid(row=1, column=0, sticky="w", padx=100)

    conv_btn = CTkButton(main, text="Convert", cursor="hand2", command=convert, width=60)
    conv_btn.grid(row=1, column=0, sticky="w", padx=335)
    voice_opt.set("Male")

    entry_box = CTkTextbox(main, font=("Helvita 20", 15), height=290, width=400, fg_color="grey20")
    entry_box.grid(row=2, column=0, sticky="w")
    voice_speed_text = CTkLabel(main, text="Voice Speed")
    voice_speed_text.grid(row=3, column=0, sticky="w", padx=160)
    voice_speed_show = CTkLabel(main, textvariable=voice_speed_var, width=30)
    voice_speed_show.grid(row=3, column=0, sticky="w", padx=370)
    voice_speed = CTkSlider(main, from_=0, to=125, variable=voice_speed_var, width=100)
    voice_speed.grid(row=3, column=0, sticky="w", padx=270)

    main.mainloop()


if __name__ == '__main__':
    main_win()