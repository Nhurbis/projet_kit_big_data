

from view.task_view import create_gradio_interface


if __name__ == "__main__":
    iface = create_gradio_interface()
    iface.launch(server_name="0.0.0.0")
