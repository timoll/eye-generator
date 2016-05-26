Blendermake: generate.py
	blender base.blend -b -P generate.py
clean:
	find *.blen* | grep -v 'base\.blend$$' | xargs rm
