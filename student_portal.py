"""Student Portal - front-end-only Tkinter application.

All data lives in memory; nothing is persisted or fetched from a server.
Run with:  python3 student_portal.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

FONT = "Helvetica Neue"

C = {
    "sidebar": "#1e2a45", "sidebar_hover": "#29395f", "sidebar_active": "#314670",
    "sidebar_text": "#a3b0cc", "accent": "#4f8dff", "bg": "#eef1f6",
    "card": "#ffffff", "border": "#dfe4ec", "text": "#212a37", "muted": "#8490a3",
    "track": "#e8ecf3", "green": "#2fbf8f", "blue": "#4f8dff", "orange": "#f5a623",
    "red": "#e05d5d", "purple": "#8e6ee0", "teal": "#22b8b8",
}

STUDENT = {
    "name": "Gottipati Pallavi", "sid": "RA2511026010986",
    "program": "B.Tech — Computer Science & Engineering",
    "semester": "Fall 2026 · Semester 3",
    "email": "pallavi.gottipati@srmist.edu.in", "phone": "+1 (555) 014-8852",
    "address": "SRM University, Kattankulathur, Chennai",
    "advisor": "Dr. Kalpana C", "gpa": "8.60", "attendance": 82,
    "credits_done": 42, "credits_total": 160, "enrolled": "August 2024",
}

COURSES = [
    {"code": "21CSC201J", "name": "Data Structures and Algorithms", "instructor": "Dr. Kalpana C",
     "credits": 4, "progress": 82, "color": C["blue"], "room": "TP-403",
     "cat": "Theory & Practical", "meets": "Mon, Wed · 9:00–10:30 AM"},
    {"code": "21CSC202J", "name": "Operating Systems", "instructor": "Dr. Pavithra L",
     "credits": 4, "progress": 78, "color": C["red"], "room": "TP-511",
     "cat": "Theory & Practical", "meets": "Tue, Thu · 9:00–10:30 AM"},
    {"code": "21CSC203P", "name": "Advanced Programming Practice", "instructor": "Syed Abuthahir S",
     "credits": 4, "progress": 78, "color": C["teal"], "room": "Lab TP-7",
     "cat": "Professional Core", "meets": "Mon 11:00 AM–12:30 PM · Wed 2:00–4:00 PM"},
    {"code": "21MAB201T", "name": "Transforms and Boundary Value Problems", "instructor": "Dr. R. Mahendran",
     "credits": 4, "progress": 79, "color": C["orange"], "room": "UB-1203",
     "cat": "Basic Science", "meets": "Mon 2:00–3:30 · Wed 11:00 AM–12:30 PM"},
    {"code": "21CSS201T", "name": "Computer Organization and Architecture", "instructor": "Dr. Anousouya Devi M",
     "credits": 4, "progress": 90, "color": C["purple"], "room": "UB-908",
     "cat": "Engineering Science", "meets": "Tue, Thu · 11:00 AM–12:30 PM"},
    {"code": "21LEM201T", "name": "Professional Ethics", "instructor": "Dr. K. Ezhil",
     "credits": 1, "progress": 100, "color": C["green"], "room": "UB-701",
     "cat": "Mandatory", "meets": "Tue · 2:00–3:00 PM"},
    {"code": "21LEM202T", "name": "UHV-II: Universal Human Values", "instructor": "Dr. Gopirajan PV",
     "credits": 3, "progress": 100, "color": "#c2549a", "room": "Seminar Hall",
     "cat": "Mandatory", "meets": "Fri · 4:00–5:00 PM"},
]

SCHEDULE = {
    "Mon": [(540, 630, "21CSC201J", "TP-403"), (660, 750, "21CSC203P", "Lab TP-7"),
            (840, 930, "21MAB201T", "UB-1203")],
    "Tue": [(540, 630, "21CSC202J", "TP-511"), (660, 750, "21CSS201T", "UB-908"),
            (840, 900, "21LEM201T", "UB-701")],
    "Wed": [(540, 630, "21CSC201J", "TP-403"), (660, 750, "21MAB201T", "UB-1203"),
            (840, 960, "21CSC203P", "Lab TP-7")],
    "Thu": [(540, 630, "21CSC202J", "TP-511"), (660, 750, "21CSS201T", "UB-908")],
    "Fri": [(480, 570, "21CSC203P", "Lab TP-7"), (600, 690, "21CSC201J", "TP-403"),
            (780, 870, "21MAB201T", "UB-1203"), (900, 990, "21CSC202J", "TP-511"),
            (990, 1020, "21LEM202T", "Seminar Hall")],
}

GRADES = [
    ("21MAB201T", "Internals — published", "18.6/35", "C"),
    ("21CSC201J", "Internals — published", "76.4/100", "A"),
    ("21CSS201T", "Internals — published", "71.5/100", "A"),
    ("21CSC203P", "Internals — published", "90.0/100", "A+"),
    ("21CSC202J", "Internals — published", "61.4/100", "B+"),
    ("21LEM201T", "Internals — published", "100/100", "O"),
    ("21LEM202T", "Internals", "Awaiting result", "—"),
]

STANDINGS = [("21LEM201T", 100, "O"), ("21CSC203P", 90, "A+"),
             ("21CSC201J", 76, "A"), ("21CSS201T", 72, "A"),
             ("21CSC202J", 61, "B+"), ("21MAB201T", 53, "C")]

DEADLINES = [
    ("21CSC203P", "APP — weekly coding set 6", "Sat, Nov 8", "2 days", C["red"]),
    ("21MAB201T", "Tutorial sheet — PDE transforms", "Sun, Nov 9", "3 days", C["orange"]),
    ("21CSC201J", "DSA — AVL tree lab record", "Mon, Nov 10", "4 days", C["orange"]),
    ("21CSC202J", "OS — scheduling algorithms quiz", "Wed, Nov 12", "6 days", C["blue"]),
    ("21CSS201T", "COA — ALU design review", "Fri, Nov 14", "8 days", C["green"]),
]

ANNOUNCEMENTS = [
    ("Academic", C["blue"], "Semester 3 internals published", "CoE Office · Nov 5",
     "Internal assessment marks for all Semester 3 courses are now available "
     "under Marks. Contact your course faculty within 7 days for re-evaluation."),
    ("Event", C["purple"], "Deepavali — university holiday", "Registrar · Nov 4",
     "Saturday, Nov 8 is a university holiday on account of Deepavali. Classes "
     "resume on Monday, Nov 9 as per Day Order 4."),
    ("Deadline", C["orange"], "Nov 20 — last working day", "CoE Office · Nov 3",
     "Friday, Nov 20 is the last working day for B.Tech II/III/IV years. Plan "
     "your submissions and lab records accordingly."),
    ("Alert", C["red"], "Portal maintenance this Saturday", "IT Services · Nov 4",
     "Campus Web will be offline on Saturday, Nov 8 from 2:00–4:00 AM for "
     "scheduled maintenance. Save any work in progress beforehand."),
    ("General", C["teal"], "Hostel mess menu updated", "Campus Life · Oct 30",
     "The November mess menu is live under Campus Life → Mess. Veg and non-veg "
     "options rotate weekly."),
]

COURSE_COLOR = {c["code"]: c["color"] for c in COURSES}


# ------------------------------------------------------------ widget helpers

def _rgb(h):
    return tuple(int(h.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))


def tint(h, f=0.85):
    return "#%02x%02x%02x" % tuple(int(v + (255 - v) * f) for v in _rgb(h))


def shade(h, f=0.82):
    return "#%02x%02x%02x" % tuple(int(v * f) for v in _rgb(h))


def initials(name):
    return "".join(p[0] for p in name.split()[:2]).upper()


def fmt_time(mins):
    h, m = divmod(mins, 60)
    return "%d:%02d %s" % (h % 12 or 12, m, "AM" if h < 12 else "PM")


def F(parent, bg=None, **kw):
    return tk.Frame(parent, bg=bg or C["card"], **kw)


def L(parent, text, bg=None, fg=None, s=11, w="normal", **kw):
    return tk.Label(parent, text=text, bg=bg or C["card"], fg=fg or C["text"],
                    font=(FONT, s, w), **kw)


def card(parent, **kw):
    return F(parent, highlightthickness=1, highlightbackground=C["border"], bd=0, **kw)


def pill(parent, text, color):
    return L(parent, text, tint(color, 0.88), shade(color, 0.62), 9, "bold",
             padx=8, pady=3)


def hbar(parent, frac, color, w=220, h=8, bg="#ffffff"):
    cv = tk.Canvas(parent, width=w, height=h, bg=bg, highlightthickness=0, bd=0)
    cv.create_rectangle(0, 0, w, h, fill=C["track"], outline="")
    if frac > 0:
        cv.create_rectangle(0, 0, max(h, int(w * frac)), h, fill=color, outline="")
    return cv


def divider(parent, color=None):
    return F(parent, bg=color or C["border"], height=1)


def logo(parent, size, text_size, bg=C["sidebar"]):
    cv = tk.Canvas(parent, width=size, height=size, bg=bg, highlightthickness=0)
    cv.create_oval(1, 1, size - 1, size - 1, fill=C["accent"], outline="")
    cv.create_text(size / 2, size / 2 + 1, text="SR", fill="#ffffff",
                   font=(FONT, text_size, "bold"))
    return cv


class FlatButton(tk.Label):
    """Colored clickable label — tk.Button can't do flat colored styles on macOS."""

    def __init__(self, master, text, command=None, bg=C["accent"], fg="#ffffff",
                 hover=None, font=(FONT, 11, "bold"), padx=16, pady=8):
        super().__init__(master, text=text, bg=bg, fg=fg, font=font,
                         padx=padx, pady=pady, cursor="hand2")
        self._command, self._bg = command, bg
        self._hover = hover or shade(bg, 0.86)
        self.bind("<Enter>", lambda e: self.config(bg=self._hover))
        self.bind("<Leave>", lambda e: self.config(bg=self._bg))
        self.bind("<Button-1>", lambda e: self._command and self._command())

    def set_colors(self, bg, fg=None):
        self._bg, self._hover = bg, shade(bg, 0.86)
        self.config(bg=bg)
        if fg is not None:
            self.config(fg=fg)


class ScrollFrame(tk.Frame):
    """Scrollable container that tracks mouse-wheel and content size."""

    def __init__(self, master, bg):
        super().__init__(master, bg=bg)
        self.canvas = tk.Canvas(self, bg=bg, highlightthickness=0, bd=0)
        self.vbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.inner = F(self.canvas, bg=bg)
        self._win = self.canvas.create_window((0, 0), window=self.inner, anchor="nw")
        self.canvas.configure(yscrollcommand=self.vbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.inner.bind("<Configure>", lambda e: self._sync())
        self.canvas.bind("<Configure>", lambda e: self._sync(e.width))
        self.canvas.bind("<Enter>", lambda e: self.canvas.bind_all("<MouseWheel>", self._wheel))
        self.canvas.bind("<Leave>", lambda e: self.canvas.unbind_all("<MouseWheel>"))

    def _sync(self, width=None):
        if width:
            self.canvas.itemconfig(self._win, width=width)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        needs = self.inner.winfo_reqheight() > self.canvas.winfo_height()
        if needs and not self.vbar.winfo_ismapped():
            self.vbar.pack(side="right", fill="y")
        elif not needs and self.vbar.winfo_ismapped():
            self.vbar.pack_forget()

    def _wheel(self, e):
        if self.canvas.winfo_exists():
            self.canvas.yview_scroll(int(-e.delta), "units")


class StudentPortal(tk.Tk):

    NAV = [("Dashboard", "dashboard"), ("My Courses", "courses"),
           ("Grades", "grades"), ("Schedule", "schedule"),
           ("Announcements", "announcements"), ("Profile", "profile")]

    def __init__(self):
        super().__init__()
        self.title("SRM University — Student Portal")
        self.configure(bg=C["bg"])
        self.minsize(1120, 700)
        w, h = 1180, 740
        self.geometry("%dx%d+%d+%d" % (w, h, (self.winfo_screenwidth() - w) // 2,
                                       (self.winfo_screenheight() - h) // 2))
        st = ttk.Style(self)
        if "clam" in st.theme_names():
            st.theme_use("clam")
        st.configure("Treeview", rowheight=34, font=(FONT, 11), background="#ffffff",
                     fieldbackground="#ffffff", foreground=C["text"], borderwidth=0)
        st.configure("Treeview.Heading", font=(FONT, 10, "bold"), background="#f4f6fa",
                     foreground=C["muted"], relief="flat", borderwidth=0, padding=(8, 8))
        st.map("Treeview", background=[("selected", "#e8efff")],
               foreground=[("selected", C["text"])])
        st.configure("Vertical.TScrollbar", background="#dfe4ec", troughcolor=C["bg"],
                     bordercolor=C["bg"], arrowcolor=C["muted"], relief="flat")
        self.current, self.pages, self.nav_widgets = None, {}, {}
        self._ann_filter = "All"
        self.show_login()

    def _wipe(self):
        self.unbind_all("<MouseWheel>")
        for w in self.winfo_children():
            w.destroy()

    # ---------------------------------------------------------------- login

    def show_login(self):
        self._wipe()
        left = F(self, bg=C["sidebar"])
        left.place(relx=0, rely=0, relwidth=0.42, relheight=1)
        brand = F(left, bg=C["sidebar"])
        brand.place(relx=0.5, rely=0.47, anchor="center")
        logo(brand, 66, 21).pack()
        L(brand, "SRM University", C["sidebar"], "#ffffff", 26, "bold").pack(pady=(16, 2))
        L(brand, "Student Portal — your campus, in one place.",
          C["sidebar"], C["sidebar_text"], 12).pack()
        feats = F(brand, bg=C["sidebar"])
        feats.pack(pady=(28, 0), anchor="w")
        for line in ("Check grades and transcripts", "Track deadlines and exams",
                     "Plan your weekly schedule"):
            row = F(feats, bg=C["sidebar"])
            row.pack(fill="x", pady=5)
            L(row, "✓", C["sidebar"], C["green"], 11, "bold").pack(side="left", padx=(0, 10))
            L(row, line, C["sidebar"], C["sidebar_text"]).pack(side="left")

        right = F(self, bg="#ffffff")
        right.place(relx=0.42, rely=0, relwidth=0.58, relheight=1)
        form = F(right, bg="#ffffff", width=300)
        form.place(relx=0.5, rely=0.47, anchor="center")
        L(form, "Sign in", "#ffffff", C["text"], 22, "bold").pack(anchor="w")
        L(form, "Access your student dashboard", "#ffffff", C["muted"]).pack(anchor="w", pady=(2, 10))
        self.u_entry = self._entry(form, "USERNAME", size=12, ret=True)
        self.p_entry = self._entry(form, "PASSWORD", show="•", size=12, ret=True)
        self.login_err = L(form, "", "#ffffff", C["red"], 10, anchor="w")
        self.login_err.pack(fill="x", pady=(10, 0))
        FlatButton(form, "Sign in", command=self._login, pady=10).pack(fill="x", pady=(4, 14))
        L(form, "Demo build — any credentials will work.", "#ffffff", C["muted"], 10).pack(anchor="w")
        self.u_entry.focus_set()

    def _entry(self, parent, label, show="", value="", size=11, ret=False):
        L(parent, label, C["card"], C["muted"], 9, "bold", anchor="w").pack(fill="x", pady=(10, 4))
        wrap = F(parent, bg="#f7f9fc", highlightthickness=1, highlightbackground=C["border"])
        e = tk.Entry(wrap, relief="flat", bg="#f7f9fc", fg=C["text"], font=(FONT, size),
                     insertbackground=C["text"], bd=0, show=show)
        e.pack(fill="x", padx=12, pady=8)
        wrap.pack(fill="x")
        if value:
            e.insert(0, value)
        e.bind("<FocusIn>", lambda ev: wrap.config(highlightbackground=C["accent"]))
        e.bind("<FocusOut>", lambda ev: wrap.config(highlightbackground=C["border"]))
        if ret:
            e.bind("<Return>", lambda ev: self._login())
        return e

    def _login(self):
        if not self.u_entry.get().strip() or not self.p_entry.get():
            self.login_err.config(text="Please enter your username and password.")
            return
        self.build_shell()

    # ---------------------------------------------------------------- shell

    def build_shell(self):
        self._wipe()
        shell = F(self, bg=C["bg"])
        shell.pack(fill="both", expand=True)
        self._sidebar(shell)
        self.content = F(shell, bg=C["bg"])
        self.content.pack(side="left", fill="both", expand=True)
        for _label, key in self.NAV:
            page = F(self.content, bg=C["bg"])
            page.place(relx=0, rely=0, relwidth=1, relheight=1)
            sf = ScrollFrame(page, bg=C["bg"])
            sf.pack(fill="both", expand=True)
            wrap = F(sf.inner, bg=C["bg"], padx=28, pady=24)
            wrap.pack(fill="both", expand=True)
            self.pages[key] = page
            getattr(self, "_build_" + key)(wrap)
        self.show_page("dashboard")

    def _sidebar(self, parent):
        sb = F(parent, bg=C["sidebar"], width=232)
        sb.pack(side="left", fill="y")
        sb.pack_propagate(False)
        top = F(sb, bg=C["sidebar"])
        top.pack(fill="x", padx=20, pady=(24, 16))
        logo(top, 34, 12).pack(side="left")
        names = F(top, bg=C["sidebar"])
        names.pack(side="left", padx=(10, 0))
        L(names, "SRM University", C["sidebar"], "#ffffff", 14, "bold", anchor="w").pack(fill="x")
        L(names, "STUDENT PORTAL", C["sidebar"], C["sidebar_text"], 8, "bold", anchor="w").pack(fill="x")

        nav = F(sb, bg=C["sidebar"])
        nav.pack(fill="x", padx=12, pady=(8, 0))
        self.nav_widgets = {}
        for label, key in self.NAV:
            row = F(nav, bg=C["sidebar"], cursor="hand2")
            row.pack(fill="x", pady=2)
            bar = F(row, bg=C["sidebar"], width=3)
            bar.pack(side="left", fill="y")
            txt = L(row, label, C["sidebar"], C["sidebar_text"], 11, "bold",
                    anchor="w", padx=14, pady=10)
            txt.pack(side="left", fill="x", expand=True)
            self.nav_widgets[key] = (row, bar, txt)
            for w in (row, bar, txt):
                w.bind("<Button-1>", lambda e, k=key: self.show_page(k))
                w.bind("<Enter>", lambda e, k=key: self._nav_hover(k, True))
                w.bind("<Leave>", lambda e, k=key: self._nav_hover(k, False))

        bottom = F(sb, bg=C["sidebar"])
        bottom.pack(side="bottom", fill="x", padx=16, pady=16)
        divider(bottom, "#2c3c60").pack(fill="x", pady=(0, 14))
        prof = F(bottom, bg=C["sidebar"])
        prof.pack(fill="x")
        av = tk.Canvas(prof, width=36, height=36, bg=C["sidebar"], highlightthickness=0)
        av.create_oval(1, 1, 35, 35, fill=C["accent"], outline="")
        self._side_initials = av.create_text(18, 19, text=initials(STUDENT["name"]),
                                             fill="#ffffff", font=(FONT, 12, "bold"))
        av.pack(side="left")
        who = F(prof, bg=C["sidebar"])
        who.pack(side="left", padx=(10, 0))
        self._side_name = L(who, STUDENT["name"], C["sidebar"], "#ffffff", 11, "bold", anchor="w")
        self._side_name.pack(fill="x")
        L(who, STUDENT["sid"], C["sidebar"], C["sidebar_text"], 9, anchor="w").pack(fill="x")
        self._side_avatar = av
        FlatButton(bottom, "Log out", command=self._logout, bg="#2c3c60",
                   hover="#3a4c78", pady=7).pack(fill="x", pady=(14, 0))

    def _nav_paint(self, key, bgc, active=False):
        row, bar, txt = self.nav_widgets[key]
        row.config(bg=bgc)
        bar.config(bg=C["accent"] if active else bgc)
        txt.config(bg=bgc, fg="#ffffff" if active else C["sidebar_text"])

    def _nav_hover(self, key, on):
        if key != self.current:
            self._nav_paint(key, C["sidebar_hover"] if on else C["sidebar"])

    def show_page(self, key):
        self.pages[key].tkraise()
        self.current = key
        for k in self.nav_widgets:
            self._nav_paint(k, C["sidebar_active"] if k == key else C["sidebar"], k == key)

    def _logout(self):
        self.pages, self.nav_widgets, self.current = {}, {}, None
        self.show_login()

    # ---------------------------------------------------- shared page pieces

    def _page_title(self, wrap, title, subtitle):
        L(wrap, title, C["bg"], C["text"], 20, "bold", anchor="w").pack(fill="x")
        L(wrap, subtitle, C["bg"], C["muted"], anchor="w").pack(fill="x", pady=(2, 0))
        F(wrap, bg=C["bg"], height=18).pack()

    def _stat_card(self, parent, label, value, sub=None, frac=None, frac_color=None):
        c = card(parent)
        inner = F(c, padx=18, pady=16)
        inner.pack(fill="both", expand=True)
        L(inner, label.upper(), fg=C["muted"], s=9, w="bold", anchor="w").pack(fill="x")
        L(inner, value, s=22, w="bold", anchor="w").pack(fill="x", pady=(2, 0))
        if frac is not None:
            hbar(inner, frac, frac_color or C["accent"], w=170, h=7).pack(anchor="w", pady=(8, 0))
        if sub:
            L(inner, sub, fg=C["muted"], s=10, anchor="w").pack(fill="x", pady=(6, 0))
        return c

    def _card_header(self, c, title, right_text=None):
        inner = F(c, padx=18)
        inner.pack(fill="x", pady=(14, 0))
        L(inner, title, s=13, w="bold").pack(side="left")
        if right_text:
            L(inner, right_text, fg=C["muted"], s=10, w="bold").pack(side="right")

    def _section(self, parent, title, right_text=None, padx=18, pady=12, expand=False):
        c = card(parent)
        self._card_header(c, title, right_text)
        body = F(c, padx=padx, pady=pady)
        body.pack(fill="both" if expand else "x", expand=expand)
        return c, body

    def _cols(self, wrap, weights, tag, pady=0):
        mid = F(wrap, bg=C["bg"])
        mid.pack(fill="x", pady=pady)
        for i, w in enumerate(weights):
            mid.columnconfigure(i, weight=w, uniform=tag)
        return mid

    def _dialog(self, title, w, h):
        top = tk.Toplevel(self)
        top.title(title)
        top.configure(bg="#ffffff")
        top.resizable(False, False)
        top.transient(self)
        top.geometry("%dx%d+%d+%d" % (w, h, self.winfo_rootx() + (self.winfo_width() - w) // 2,
                                      self.winfo_rooty() + (self.winfo_height() - h) // 2))
        return top

    def _kv_rows(self, parent, pairs, lw=12):
        for lab, val in pairs:
            r = F(parent, bg="#ffffff")
            r.pack(fill="x", pady=3)
            L(r, lab, "#ffffff", C["muted"], 10, "bold", width=lw, anchor="w").pack(side="left")
            L(r, val, "#ffffff", C["text"], 11, anchor="w").pack(side="left")

    # ------------------------------------------------------------ dashboard

    def _build_dashboard(self, wrap):
        hour = datetime.now().hour
        greet = "Good morning" if hour < 12 else "Good afternoon" if hour < 18 else "Good evening"
        banner = F(wrap, bg=C["accent"])
        banner.pack(fill="x", pady=(0, 16))
        inner = F(banner, bg=C["accent"], padx=24, pady=20)
        inner.pack(fill="x")
        leftcol = F(inner, bg=C["accent"])
        leftcol.pack(side="left", fill="x", expand=True)
        L(leftcol, "%s, %s" % (greet, STUDENT["name"].split()[0]), C["accent"],
          "#ffffff", 20, "bold", anchor="w").pack(fill="x")
        L(leftcol, "Here is your snapshot for %s." % datetime.now().strftime("%A, %B %d, %Y"),
          C["accent"], "#dbe7ff", anchor="w").pack(fill="x", pady=(3, 0))
        L(inner, STUDENT["semester"], shade(C["accent"], 0.82), "#ffffff", 10,
          "bold", padx=14, pady=6).pack(side="right", anchor="ne")

        stats = F(wrap, bg=C["bg"])
        stats.pack(fill="x", pady=(0, 16))
        for i in range(4):
            stats.columnconfigure(i, weight=1, uniform="st")
        cards = [
            ("SGPA", STUDENT["gpa"], "Projected · published subjects", None, None),
            ("Credits", "%d / %d" % (STUDENT["credits_done"], STUDENT["credits_total"]),
             "On track for 2028", STUDENT["credits_done"] / STUDENT["credits_total"], C["accent"]),
            ("Attendance", "%d%%" % STUDENT["attendance"], "258 / 313 classes · all on track",
             STUDENT["attendance"] / 100.0, C["green"]),
            ("Courses", str(len(COURSES)), "2 labs · 4 lectures", None, None),
        ]
        for i, (lab, val, sub, frac, fc) in enumerate(cards):
            self._stat_card(stats, lab, val, sub, frac, fc).grid(
                row=0, column=i, sticky="nsew", padx=(0, 8 if i < 3 else 0))

        mid = self._cols(wrap, (3, 2), "m", pady=(0, 16))

        dl, body = self._section(mid, "Upcoming deadlines", "%d due" % len(DEADLINES), pady=8)
        dl.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        body.columnconfigure(1, weight=1)
        for i, (code, task, due, due_in, urgent) in enumerate(DEADLINES):
            L(body, "●", fg=COURSE_COLOR[code], s=10).grid(row=i * 2, column=0, padx=(0, 10))
            txt = F(body)
            txt.grid(row=i * 2, column=1, sticky="w")
            L(txt, task, s=11, w="bold", anchor="w").pack(fill="x")
            L(txt, "%s · %s" % (code, due), fg=C["muted"], s=10, anchor="w").pack(fill="x")
            pill(body, due_in, urgent).grid(row=i * 2, column=2, sticky="e", padx=(10, 0))
            if i < len(DEADLINES) - 1:
                divider(body).grid(row=i * 2 + 1, column=0, columnspan=3, sticky="ew", pady=8)

        right = F(mid, bg=C["bg"])
        right.grid(row=0, column=1, sticky="nsew")
        an, ab = self._section(right, "Announcements", pady=8)
        an.pack(fill="x", pady=(0, 14))
        for i, (cat, col, title, meta, _b) in enumerate(ANNOUNCEMENTS[:3]):
            row = F(ab)
            row.pack(fill="x", pady=(4 if i else 0, 6))
            L(row, "●", fg=col, s=10).pack(side="left", padx=(0, 10), anchor="n", pady=2)
            tx = F(row)
            tx.pack(side="left", fill="x", expand=True)
            L(tx, title, s=11, w="bold", anchor="w", wraplength=270, justify="left").pack(fill="x")
            L(tx, meta, fg=C["muted"], s=9, anchor="w").pack(fill="x")
        FlatButton(an, "View all →", command=lambda: self.show_page("announcements"),
                   bg=tint(C["accent"], 0.88), fg=shade(C["accent"], 0.7),
                   hover=tint(C["accent"], 0.8), font=(FONT, 10, "bold"),
                   padx=12, pady=6).pack(side="right", padx=18, pady=(0, 14))

        day = datetime.now().strftime("%a")
        today, tb = self._section(right, "Today's classes", day.upper(), pady=8)
        today.pack(fill="x")
        blocks = SCHEDULE.get(day, [])
        if not blocks:
            L(tb, "No classes scheduled today.", fg=C["muted"], s=10, anchor="w").pack(fill="x", pady=4)
        for s, e, code, room in blocks:
            row = F(tb)
            row.pack(fill="x", pady=5)
            L(row, "%s – %s" % (fmt_time(s), fmt_time(e)), s=10, w="bold",
              width=17, anchor="w").pack(side="left")
            L(row, code, fg=COURSE_COLOR[code], s=10, w="bold", width=10, anchor="w").pack(side="left")
            L(row, room, fg=C["muted"], s=10, anchor="w").pack(side="left")
        F(tb, height=8).pack()

        prog, pb = self._section(wrap, "Attendance by course", "Fall 2026", pady=10)
        prog.pack(fill="x")
        pb.columnconfigure(2, weight=1)
        for i, crs in enumerate(COURSES):
            L(pb, crs["code"], fg=crs["color"], s=10, w="bold", width=10,
              anchor="w").grid(row=i, column=0, sticky="w", pady=5)
            L(pb, crs["name"], fg=C["muted"], s=10, width=34, anchor="w").grid(row=i, column=1, sticky="w")
            hbar(pb, crs["progress"] / 100.0, crs["color"], w=220, h=7).grid(
                row=i, column=2, sticky="w", padx=(6, 0))
            L(pb, "%d%%" % crs["progress"], s=10, w="bold", width=5, anchor="e").grid(row=i, column=3, sticky="e")

    # ------------------------------------------------------------- courses

    def _build_courses(self, wrap):
        head = F(wrap, bg=C["bg"])
        head.pack(fill="x", pady=(0, 14))
        t = F(head, bg=C["bg"])
        t.pack(side="left")
        L(t, "My Courses", C["bg"], C["text"], 20, "bold", anchor="w").pack(fill="x")
        L(t, "%d courses · %d credits this semester"
          % (len(COURSES), sum(c["credits"] for c in COURSES)),
          C["bg"], C["muted"], anchor="w").pack(fill="x", pady=(2, 0))

        self._search_var = tk.StringVar()
        self._ph = True
        swrap = F(head, bg="#f7f9fc", highlightthickness=1, highlightbackground=C["border"])
        entry = tk.Entry(swrap, textvariable=self._search_var, relief="flat", bg="#f7f9fc",
                         fg=C["muted"], font=(FONT, 11), insertbackground=C["text"],
                         width=26, bd=0)
        entry.insert(0, "Search courses…")
        entry.pack(padx=10, pady=8)
        swrap.pack(side="right")

        def on_focus(on):
            swrap.config(highlightbackground=C["accent"] if on else C["border"])
            if on and self._ph:
                entry.delete(0, "end")
                entry.config(fg=C["text"])
                self._ph = False
            elif not on and not self._search_var.get():
                entry.insert(0, "Search courses…")
                entry.config(fg=C["muted"])
                self._ph = True

        entry.bind("<FocusIn>", lambda e: on_focus(True))
        entry.bind("<FocusOut>", lambda e: on_focus(False))
        self._search_var.trace_add("write", lambda *a: self._fill_courses())
        self._course_grid = F(wrap, bg=C["bg"])
        self._course_grid.pack(fill="both", expand=True)
        for i in range(2):
            self._course_grid.columnconfigure(i, weight=1, uniform="cg")
        self._fill_courses()

    def _fill_courses(self):
        grid = self._course_grid
        for w in grid.winfo_children():
            w.destroy()
        q = "" if self._ph else self._search_var.get().strip().lower()
        items = [c for c in COURSES
                 if q in (c["code"] + " " + c["name"] + " " + c["instructor"]).lower()]
        if not items:
            L(grid, 'No courses match "%s".' % self._search_var.get(),
              C["bg"], C["muted"], 12).grid(row=0, column=0, columnspan=2, pady=50)
            return
        for i, crs in enumerate(items):
            self._course_card(grid, crs).grid(row=i // 2, column=i % 2, sticky="nsew", padx=7, pady=7)

    def _course_card(self, parent, crs):
        c = card(parent)
        inner = F(c, padx=18, pady=16)
        inner.pack(fill="both", expand=True)
        top = F(inner)
        top.pack(fill="x")
        pill(top, crs["code"], crs["color"]).pack(side="left")
        L(top, "%d credits" % crs["credits"], fg=C["muted"], s=10, w="bold").pack(side="right")
        L(inner, crs["name"], s=14, w="bold", anchor="w", wraplength=330,
          justify="left").pack(fill="x", pady=(10, 2))
        L(inner, crs["instructor"], fg=C["muted"], anchor="w").pack(fill="x")
        L(inner, "%s · Rm %s" % (crs["meets"], crs["room"]), fg=C["muted"],
          s=10, anchor="w").pack(fill="x", pady=(2, 12))
        divider(inner).pack(fill="x")
        bot = F(inner)
        bot.pack(fill="x", pady=(12, 0))
        hbar(bot, crs["progress"] / 100.0, crs["color"], w=170, h=7).pack(side="left", pady=4)
        L(bot, "%d%%" % crs["progress"], s=10, w="bold").pack(side="left", padx=(8, 0))
        FlatButton(bot, "Details →", command=lambda: self._open_course(crs),
                   bg=tint(crs["color"], 0.88), fg=shade(crs["color"], 0.65),
                   hover=tint(crs["color"], 0.78), font=(FONT, 10, "bold"),
                   padx=12, pady=5).pack(side="right")
        return c

    def _open_course(self, crs):
        top = self._dialog("%s — %s" % (crs["code"], crs["name"]), 460, 480)
        F(top, bg=crs["color"], height=6).pack(fill="x")
        body = F(top, bg="#ffffff", padx=24, pady=20)
        body.pack(fill="both", expand=True)
        head = F(body, bg="#ffffff")
        head.pack(fill="x")
        pill(head, crs["code"], crs["color"]).pack(side="left")
        pill(head, "Enrolled", C["green"]).pack(side="left", padx=(8, 0))
        L(body, crs["name"], "#ffffff", C["text"], 16, "bold", anchor="w",
          wraplength=400, justify="left").pack(fill="x", pady=(10, 14))
        self._kv_rows(body, [("Instructor", crs["instructor"]), ("Credits", str(crs["credits"])),
                             ("Schedule", crs["meets"]), ("Room", crs["room"]),
                             ("Category", crs["cat"])])
        pr = F(body, bg="#ffffff")
        pr.pack(fill="x", pady=(14, 0))
        L(pr, "Progress", "#ffffff", C["muted"], 10, "bold", width=12, anchor="w").pack(side="left")
        hbar(pr, crs["progress"] / 100.0, crs["color"], w=190, h=8).pack(side="left", pady=3)
        L(pr, "%d%% complete" % crs["progress"], "#ffffff", C["text"], 10, "bold").pack(side="left", padx=(10, 0))
        divider(body).pack(fill="x", pady=18)
        FlatButton(body, "Close", command=top.destroy, bg="#edf1f7",
                   fg=C["text"], hover="#e2e8f0").pack(side="right")
        FlatButton(body, "View syllabus", bg=tint(crs["color"], 0.88),
                   fg=shade(crs["color"], 0.65), hover=tint(crs["color"], 0.78),
                   command=lambda: messagebox.showinfo(
                       "Syllabus", "The syllabus for %s is not attached in this demo build."
                       % crs["code"], parent=top)).pack(side="right", padx=(0, 10))

    # -------------------------------------------------------------- grades

    def _build_grades(self, wrap):
        self._page_title(wrap, "Grades", "Semester 3 · internals — 140.5 / 193 marks earned")
        stats = F(wrap, bg=C["bg"])
        stats.pack(fill="x", pady=(0, 16))
        for i in range(3):
            stats.columnconfigure(i, weight=1, uniform="gs")
        cards = [
            ("CGPA", STUDENT["gpa"], "Projected · 10-pt scale", None, None),
            ("Credits earned", str(STUDENT["credits_done"]),
             "of %d required" % STUDENT["credits_total"],
             STUDENT["credits_done"] / STUDENT["credits_total"], C["accent"]),
            ("Best grade", "O", "Professional Ethics · 100%", None, None),
        ]
        for i, (lab, val, sub, frac, fc) in enumerate(cards):
            self._stat_card(stats, lab, val, sub, frac, fc).grid(
                row=0, column=i, sticky="nsew", padx=(0, 8 if i < 2 else 0))

        mid = self._cols(wrap, (3, 2), "gr")

        tc, tf = self._section(mid, "Assignment results", "double-click a row",
                               padx=10, pady=10, expand=True)
        tc.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        tree = ttk.Treeview(tf, columns=("course", "assignment", "score", "grade"),
                            show="headings", height=11)
        for col, text, w, anc in (("course", "Course", 70, "w"),
                                  ("assignment", "Assignment", 290, "w"),
                                  ("score", "Score", 80, "center"), ("grade", "Grade", 60, "center")):
            tree.heading(col, text=text)
            tree.column(col, width=w, anchor=anc)
        vsb = ttk.Scrollbar(tf, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        tree.pack(side="left", fill="both", expand=True)
        vsb.pack(side="right", fill="y")
        for i, row in enumerate(GRADES):
            tree.insert("", "end", values=row, tags=(["odd"] if i % 2 else []) + ["g_" + row[3][0]])
        tree.tag_configure("odd", background="#f7f9fc")
        for letter, fg in {"O": "#1e9e74", "A": "#1e9e74", "B": C["blue"],
                           "C": C["orange"], "D": C["red"]}.items():
            tree.tag_configure("g_" + letter, foreground=fg)
        tree.bind("<Double-Button-1>", lambda e: self._grade_detail(tree))

        sc, sb = self._section(mid, "Course standing", "overall %")
        sc.grid(row=0, column=1, sticky="nsew")
        for code, pct, letter in STANDINGS:
            row = F(sb)
            row.pack(fill="x", pady=6)
            L(row, code, fg=COURSE_COLOR[code], s=10, w="bold", width=10, anchor="w").pack(side="left")
            hbar(row, pct / 100.0, COURSE_COLOR[code], w=150, h=7).pack(side="left", padx=(4, 8), pady=3)
            L(row, "%d%%" % pct, s=10, w="bold", width=4, anchor="w").pack(side="left")
            L(row, letter, fg=C["muted"], s=10, w="bold", width=3, anchor="e").pack(side="right")

    def _grade_detail(self, tree):
        sel = tree.selection()
        if not sel:
            return
        co, asg, sc, gr = tree.item(sel[0], "values")
        col = COURSE_COLOR.get(co, C["accent"])
        top = self._dialog("Grade detail", 380, 300)
        F(top, bg=col, height=6).pack(fill="x")
        body = F(top, bg="#ffffff", padx=24, pady=18)
        body.pack(fill="both", expand=True)
        pill(body, co, col).pack(anchor="w")
        L(body, asg, "#ffffff", C["text"], 14, "bold", anchor="w",
          wraplength=330, justify="left").pack(fill="x", pady=(10, 12))
        self._kv_rows(body, [("Score", sc), ("Grade", gr), ("Weight", "15%"),
                             ("Status", "Graded · posted Oct 30")], lw=10)
        FlatButton(body, "Close", command=top.destroy, bg="#edf1f7",
                   fg=C["text"], hover="#e2e8f0", padx=14, pady=7).pack(side="bottom", anchor="e")

    # ------------------------------------------------------------ schedule

    def _build_schedule(self, wrap):
        self._page_title(wrap, "Weekly Schedule", "Monday – Friday · 8:00 AM – 5:00 PM")
        legend = F(wrap, bg=C["bg"])
        legend.pack(fill="x", pady=(0, 10))
        for crs in COURSES:
            L(legend, "●", C["bg"], crs["color"], 10).pack(side="left", padx=(0, 4))
            L(legend, crs["code"], C["bg"], C["muted"], 10, "bold").pack(side="left", padx=(0, 14))

        c = card(wrap)
        c.pack(fill="x")
        W, GUTTER, HEADER, PX_H = 880, 56, 36, 64
        H = HEADER + 9 * PX_H + 10
        cv = tk.Canvas(c, width=W, height=H, bg=C["card"], highlightthickness=0, bd=0)
        cv.pack(padx=18, pady=14, anchor="w")
        hour0, dayw, days = 8 * 60, (W - GUTTER) / 5.0, ["Mon", "Tue", "Wed", "Thu", "Fri"]

        for d, day in enumerate(days):
            x0 = GUTTER + d * dayw
            cv.create_text(x0 + dayw / 2, 18, text=day.upper(),
                           font=(FONT, 10, "bold"), fill=C["muted"])
            if d:
                cv.create_line(x0, HEADER, x0, H, fill="#eef1f6")
        for h in range(10):
            y = HEADER + h * PX_H
            cv.create_line(GUTTER, y, W, y, fill="#eef1f6")
            cv.create_text(GUTTER - 8, y, text=fmt_time(hour0 + h * 60),
                           font=(FONT, 9), fill=C["muted"], anchor="e")
        cv.create_line(GUTTER, HEADER, GUTTER, H, fill=C["border"])

        for d, day in enumerate(days):
            for s, e, code, room in SCHEDULE.get(day, []):
                col = COURSE_COLOR[code]
                tbg = tint(col, 0.86)
                y0 = HEADER + (s - hour0) * PX_H / 60.0
                y1 = HEADER + (e - hour0) * PX_H / 60.0
                blk = F(cv, bg=tbg)
                F(blk, bg=col, width=4).pack(side="left", fill="y")
                tx = F(blk, bg=tbg)
                tx.pack(side="left", fill="both", expand=True, padx=8, pady=6)
                L(tx, code, tbg, shade(col, 0.6), 10, "bold", anchor="w").pack(fill="x")
                L(tx, "%s – %s" % (fmt_time(s), fmt_time(e)), tbg, shade(col, 0.55),
                  9, anchor="w").pack(fill="x")
                if y1 - y0 > 72:
                    L(tx, "Rm " + room, tbg, shade(col, 0.55), 9, anchor="w").pack(fill="x")
                cv.create_window(GUTTER + d * dayw + 3, y0, anchor="nw",
                                 width=dayw - 6, height=y1 - y0, window=blk)

    # -------------------------------------------------------- announcements

    def _build_announcements(self, wrap):
        self._page_title(wrap, "Announcements", "Latest news from offices around campus")
        filt = F(wrap, bg=C["bg"])
        filt.pack(fill="x", pady=(0, 12))
        self._ann_pills = {}
        for catname in ["All"] + sorted({a[0] for a in ANNOUNCEMENTS}):
            p = FlatButton(filt, catname, font=(FONT, 10, "bold"), padx=12, pady=5,
                           command=lambda n=catname: self._set_ann_filter(n))
            p.pack(side="left", padx=(0, 8))
            self._ann_pills[catname] = p
        self._ann_list = F(wrap, bg=C["bg"])
        self._ann_list.pack(fill="x")
        self._refresh_ann()

    def _set_ann_filter(self, name):
        self._ann_filter = name
        self._refresh_ann()

    def _refresh_ann(self):
        for name, p in self._ann_pills.items():
            if name == self._ann_filter:
                p.set_colors(C["accent"], "#ffffff")
            else:
                p.set_colors("#e3e8f0", C["muted"])
        for w in self._ann_list.winfo_children():
            w.destroy()
        items = [a for a in ANNOUNCEMENTS if self._ann_filter == "All" or a[0] == self._ann_filter]
        if not items:
            L(self._ann_list, "Nothing here yet.", C["bg"], C["muted"], 12).pack(pady=30)
        for cat, col, title, meta, body_text in items:
            c = card(self._ann_list)
            c.pack(fill="x", pady=6)
            row = F(c)
            row.pack(fill="x")
            F(row, bg=col, width=4).pack(side="left", fill="y")
            inner = F(row, padx=18, pady=14)
            inner.pack(side="left", fill="both", expand=True)
            top = F(inner)
            top.pack(fill="x")
            pill(top, cat, col).pack(side="left")
            L(top, meta, fg=C["muted"], s=10).pack(side="right")
            L(inner, title, s=13, w="bold", anchor="w").pack(fill="x", pady=(8, 3))
            L(inner, body_text, fg=C["muted"], anchor="w", wraplength=720,
              justify="left").pack(fill="x")

    # -------------------------------------------------------------- profile

    def _build_profile(self, wrap):
        self._page_title(wrap, "Profile", "Your personal and academic information")
        mid = self._cols(wrap, (2, 3), "p")

        left = card(mid)
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        inner = F(left, padx=22, pady=24)
        inner.pack(fill="x")
        av = tk.Canvas(inner, width=104, height=104, bg=C["card"], highlightthickness=0)
        av.create_oval(2, 2, 102, 102, fill=C["accent"], outline="")
        self._avatar_text = av.create_text(52, 54, text=initials(STUDENT["name"]),
                                           fill="#ffffff", font=(FONT, 30, "bold"))
        av.pack()
        self._avatar = av
        self._prof_name = L(inner, STUDENT["name"], s=16, w="bold")
        self._prof_name.pack(pady=(12, 2))
        L(inner, STUDENT["program"], fg=C["muted"]).pack()
        pill(inner, STUDENT["semester"], C["accent"]).pack(pady=(10, 4))
        divider(inner).pack(fill="x", pady=16)
        for lab, val in (("Register No.", STUDENT["sid"]), ("Advisor", STUDENT["advisor"]),
                         ("Enrolled", STUDENT["enrolled"]), ("Status", "● Active")):
            r = F(inner)
            r.pack(fill="x", pady=4)
            L(r, lab, fg=C["muted"], s=10, anchor="w").pack(side="left")
            L(r, val, fg=C["green"] if "●" in val else C["text"], s=10,
              w="bold", anchor="e").pack(side="right")

        right, form = self._section(mid, "Personal information")
        right.grid(row=0, column=1, sticky="nsew")
        self._prof_fields = {key: self._entry(form, lab.upper(), value=STUDENT[key])
                             for lab, key in (("Full name", "name"), ("Email", "email"),
                                              ("Phone", "phone"), ("Address", "address"))}
        foot = F(right, padx=18, pady=14)
        foot.pack(fill="x")
        self._save_fb = L(foot, "", s=10, w="bold")
        self._save_fb.pack(side="left")
        FlatButton(foot, "Save changes", command=self._save_profile).pack(side="right")

    def _save_profile(self):
        vals = {k: e.get().strip() for k, e in self._prof_fields.items()}
        if not vals["name"]:
            self._save_fb.config(text="Name cannot be empty.", fg=C["red"])
            return
        STUDENT.update(vals)
        init = initials(STUDENT["name"])
        self._side_name.config(text=STUDENT["name"])
        self._side_avatar.itemconfig(self._side_initials, text=init)
        self._avatar.itemconfig(self._avatar_text, text=init)
        self._prof_name.config(text=STUDENT["name"])
        self._save_fb.config(text="✓ Saved", fg=C["green"])
        fb = self._save_fb
        self.after(2400, lambda: fb.config(text="") if fb.winfo_exists() else None)


if __name__ == "__main__":
    StudentPortal().mainloop()
