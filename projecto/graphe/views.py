import paho.mqtt.client as mqtt
from django.shortcuts import render, redirect
from .models import Team, SensorData
from django.http import JsonResponse

client = mqtt.Client()


client.username_pw_set("xxjfwlqo:xxjfwlqo", "9agKXHW-5duIFt7ehaLp6JSM4-L-SMkc")
client.connect("fly.rmq.cloudamqp.com", 1883, 60)



def team_name(request):
    if request.method == 'POST':
        team_name = request.POST.get('team_name')
        team, created = Team.objects.get_or_create(name=team_name)
        return redirect('data', team_id=team.id)
    return render(request, 'team_name.html')

def data(request, team_id):

    team = Team.objects.get(id=team_id)
    td = SensorData.objects.filter(team=team)

    labels = []
    data = []

    for entry in td:
        labels.append(entry.timestamp.strftime('%H:%M:%S'))
        data.append(entry.data)

    chart_data = {
        'labels': labels,
        'data': data,
    }


    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("test")

    def on_message(client, userdata, msg):
        messa = msg.payload.decode()
        print(messa)
        SensorData.objects.create(team=team, data=messa)


    client.on_connect = on_connect
    client.on_message = on_message
    
    if request.method == 'POST':
        if 'start' in request.POST:
            receiving_data = True
            print("start")
            client.loop_start()

        elif 'stop' in request.POST:
            receiving_data = False
            print("stop")
            client.loop_stop()
    return render(request, 'data.html', {'team': team, 'td': td, 'chart_data': chart_data})

def chart(request):

    team = Team.objects.get(pk=9)
    sensor_data = SensorData.objects.filter(team=team)
    labels = []
    data = []

    for entry in sensor_data:
        labels.append(entry.timestamp.strftime('%Y-%m-%d %H:%M:%S'))
        data.append(entry.data)

    chart_data = {
        'labels': labels,
        'data': data,
    }


    return render(request, 'chart.html', {'chart_data': chart_data})

def sensor_data_json(request, team_id):
    sensor_data = SensorData.objects.filter(team_id=team_id)
    labels = [data.timestamp.strftime('%H:%M:%S') for data in sensor_data]
    data = [float(data.data) for data in sensor_data]
    return JsonResponse({'labels': labels, 'data': data})

def delete_feed(request, team_id):
    sensor_data = SensorData.objects.filter(team_id=team_id)
    sensor_data.delete()
    return redirect('data', team_id=team_id)
