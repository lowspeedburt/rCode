# > library(ggplot2)
# > ggplot(d[7:nrow(d),], aes(x=time, y=GSR))+geom_line(group=1)
# > ggplot(d[7:nrow(d),], aes(x=time, y=GSR))+geom_point(group=1)
# > ggplot(d[7:nrow(d),], aes(x=time, y=GSR))+geom_point(group=1)
# > ggplot(d[7:nrow(d),], aes(x=time, y=GSR))+geom_line(group=1)
# > ggplot(d[7:nrow(d),], aes(x=time, y=GSR))+geom_line(group=1, size=2)
# > ggplot(d[7:nrow(d),], aes(x=time, y=GSR))+geom_line(group=1, size=2, color=blue)
# Error in layer(data = data, mapping = mapping, stat = stat, geom = GeomLine,  :
#   object 'blue' not found
# > ggplot(d[7:nrow(d),], aes(x=time, y=GSR))+geom_line(group=1, size=2, color="blue")
# > ggplot(d[7:nrow(d),], aes(x=time, y=GSR))+geom_line(group=1, size=2, color="blue")+ylim(525, 600)
#
print("happy face :)")