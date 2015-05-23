#!/usr/bin/env python3
n, m, k = map(int, input().split(' '))
a = map(int, input().split(' ')) # initial app order
b = map(int, input().split(' ')) # launch order

pos_app_id = {}
app_id_pos = {}
for pos, app_id in enumerate(a):
	pos_app_id[app_id] = pos
	app_id_pos[pos] = app_id

def rotate_left(a_id):
	a_pos = pos_app_id[a_id]
	if a_pos > 0:
		b_pos = a_pos - 1
		b_id = app_id_pos[b_pos]

		pos_app_id[a_id] = b_pos
		pos_app_id[b_id] = a_pos

		app_id_pos[a_pos] = b_id
		app_id_pos[b_pos] = a_id

swipes = 0
for app_id in b:
	app_pos = pos_app_id[app_id]
	swipes += app_pos // k + 1
	rotate_left(app_id)

print(swipes)