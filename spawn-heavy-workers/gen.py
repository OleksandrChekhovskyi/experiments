f = open('worker.js', 'w')
f.write('// A lot of functions to simulate typical Emscripten output\n')

for i in range(0, 100000):
	f.write('function func{}(a) {{ return a + {}; }}\n'.format(i, i))

f.write('onmessage = function(e) { postMessage({ index: e.data.index }); };\n')
