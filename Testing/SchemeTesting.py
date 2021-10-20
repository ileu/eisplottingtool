import schemdraw as sd
from schemdraw import dsp, elements as elm

elm.style(elm.STYLE_IEC)
d = sd.Drawing(fontsize=14)
d.push()
d += dsp.Line().up().length(d.unit/4)
d += dsp.Line().length(d.unit/4)
# d += dsp.Line().right().length(d.unit/8)
d += elm.Resistor().right().length(d.unit/1.5)
d.pop()
d += dsp.Line().down().length(d.unit/4)
# d += dsp.Line().right().length(d.unit/8)
d += elm.CPE().right().length(d.unit/1.5)
# d += dsp.Line().right().length(d.unit/8)
d += dsp.Line().up().length(d.unit/4)
d.push()
d += dsp.Line().up().length(d.unit / 4)
# d += dsp.Line().left().length(d.unit / 8)
d.pop()
d += dsp.Line().right().length(d.unit/4)
d.draw()

