from flet import *

def main(page: Page):
    page.theme_mode = ThemeMode.LIGHT
    page.title = "TheEthicalVideo"
    page.window.always_on_top = True
    page.spacing = 20
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    def pick_files_result(e: FilePickerResultEvent):
        play.controls.clear()
        path = (
            ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
        )
        pat = ""
        for i in path:
            if i == "\\":
                pat += "\\"
            pat += i
        play.controls.append(
            Video(
                expand=True,
                playlist=VideoMedia(
                    pat
                ),
                playlist_mode=PlaylistMode.SINGLE,
                fill_color="#000000",
                aspect_ratio=16 / 9,
                volume=100,
                autoplay=False,
                filter_quality=FilterQuality.HIGH,
                muted=False,
            ),
        )
        page.update()

    pick_files_dialog = FilePicker(
        on_result=pick_files_result,
    )
    page.overlay.append(pick_files_dialog)

    play = Row(
        width=page.window.width-100,
        height=page.window.height-150,
    )
    alert = AlertDialog(
        content=Row(
            [
                Text("please pick file for start a video !", size=30)
            ]
        ),
        open=True,
    )
    page.overlay.append(alert)
    page.appbar = AppBar(
        title=Text("video player"),
        actions=[
            Container(
                content=Row(
                    [
                        Image(
                            "icons\\file.png",
                            width=100,
                            height=100
                        ),
                    ], alignment="center"
                ),
                on_click=lambda _: pick_files_dialog.pick_files(
                    allow_multiple=True
                ),
            )
        ]
    )
    page.add(
        play,
    )


if __name__ == '__main__':
    app(main)
