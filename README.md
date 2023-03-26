# tk_music_player

A simple music player based on tkinter

### Todos

- [ ] make it OOP
- [ ] music playlist
- [ ] select multiple files at once
- [ ] put music filetype restriction
- [ ] add music time tracker
- [ ] improve UI
- [ ] build

-------

## Notes on styling:

```python
style = ttk.Style(your_tk_root)
```

To change application style theme:

```` python
print(style.theme_names())  # get available themes for your OS
style.theme_use('alt')  # change application theme
````

to style a specific element, first you need to know the exact tkinter name of the element:

```` python
print(your_desired_element.winfo_class())
````

To find out what properties you can change in a Tkinter style, use the following commands (replace TLabel with any
other elements):

```` python
print(style.layout("TLabel"))
print(style.element_options("Label.border"))
print(style.element_options("Label.padding"))
print(style.element_options("Label.label"))
print(style.lookup("TLabel", "font"))  # current value
````

Now that you get all the requirement knowledge, you can change an element style like this:

```python
style.configure(
    "TLabel",
    font=("Segoe UI", 20),
    bordercolor="#f00",
    relief="solid"
)
```

#### *Custom Styles*

Also, ypu may want to create a custom style and use it for a specific element in multiple times. In these case:

```python
style.configure("CustomEntryStyle.TEntry", padding=20)
entry = ttk.Entry(tkMusicPlayer, style="CustomEntryStyle.TEntry")
```

to change state specific styles:
```python
style.map("CustomButtonStyle.TButton",
      foreground=[("pressed", "red"), ("active", "white")],
      background=[("pressed", "!disabled", "black"), ("active", "black")],
      )
btn = ttk.Button(tkMusicPlayer, text="Submit", style="CustomButtonStyle.TButton")
```