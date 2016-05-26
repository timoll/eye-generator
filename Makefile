Blendermake: generate.py
	blender base.blend -b -P generate.py
clean:
	find *.blen* | grep -v 'base\.blend$$' | xargs rm
render: leftDown.blend leftUp.blend rightDown.blend rightUp.blend scene.blend
	mkdir log
	nohup blender -b leftDown.blend -E CYCLES -t 5 -a </dev/null > log/renderld.log 2>&1 & 
	nohup blender -b leftUp.blend -E CYCLES -t 5 -a </dev/null > log/renderlu.log 2>&1 & 
	nohup blender -b rightDown.blend -E CYCLES -t 5 -a </dev/null > log/renderrd.log 2>&1 & 
	nohup blender -b rightUp.blend -E CYCLES -t 5 -a </dev/null > log/renderru.log 2>&1 & 
	nohup blender -b scene.blend -E CYCLES -t 5 -a </dev/null > log/renders.log 2>&1 & 
clean_render:
	rm -rf leftup leftdown rightdown rightup scene log
