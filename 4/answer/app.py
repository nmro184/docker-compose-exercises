from flask import Flask, render_template, redirect, url_for, request
import docker

app = Flask(__name__)
client = docker.from_env()

@app.route('/')
def home():
    containers = client.containers.list(all=True)
    return render_template('home.html', containers=containers)

@app.route('/create_container', methods=['GET', 'POST'])
def create_container():
    if request.method == 'POST':
        # Get form data
        container_name = request.form.get('container_name')
        image_name = request.form.get('image_name')
        host_port = int(request.form.get('host_port'))
        container_port = int(request.form.get('container_port'))

        # Create the container
        container = client.containers.run(
            image=image_name,
            name=container_name,
            detach=True,
            ports={f'{container_port}/tcp': host_port}
        )

        return redirect(url_for('home'))

    return render_template('create_container.html')

@app.route('/delete_container/<container_id>')
def delete_container(container_id):
    container = client.containers.get(container_id)
    container.stop()
    container.remove()
    return redirect(url_for('home'))


@app.route('/container_redirect/<container_id>')
def container_redirect(container_id):
    container_info = client.containers.get(container_id)
    actual_host_port = container_info.ports['80/tcp'][0]['HostPort']
    return redirect(f'http://localhost:{actual_host_port}/')


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
