SHELL=/bin/bash
CPU_CORES=$(shell grep -c ^processor /proc/cpuinfo)
CPU_RENDER=$(shell echo $(CPU_CORES)/5 | bc )
$(shell if [ ${CPU_RENDER} -lt 1 ]; then CPU_RENDER=1; fi)
Blendermake: generate.py
ifndef ANIMATION_JSON
	$(error ANIMATION_JSON is not set, set with \"export ANIMATION_JSON=yourfile.json\" before make )
endif
	@mkdir log || true
	blender base.blend -b -P generate.py -- ${ANIMATION_JSON}
clean:
	@find *.blen* | grep -v 'base\.blend$$'| grep -v 'calibrate\.blend$$' | xargs rm >/dev/null || true
render: leftDown.blend leftUp.blend rightDown.blend rightUp.blend scene.blend
	@mkdir log || true
	nohup blender -b leftDown.blend -E CYCLES -t ${CPU_RENDER} -a </dev/null > log/renderld.log 2>&1 & 
	nohup blender -b leftUp.blend -E CYCLES -t ${CPU_RENDER} -a </dev/null > log/renderlu.log 2>&1 & 
	nohup blender -b rightDown.blend -E CYCLES -t ${CPU_RENDER} -a </dev/null > log/renderrd.log 2>&1 & 
	nohup blender -b rightUp.blend -E CYCLES -t ${CPU_RENDER} -a </dev/null > log/renderru.log 2>&1 & 
	nohup blender -b scene.blend -E CYCLES -t ${CPU_RENDER} -a </dev/null > log/renders.log 2>&1 & 
clean_render:
	-rm -rf leftup leftdown rightdown rightup scene log >/dev/null
