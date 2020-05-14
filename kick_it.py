import time, datetime, random, coolname, PIL
from coolname import generate, generate_slug
from PIL import Image, ImageDraw, ImageFont

start_date = datetime.date(1997, 1, 1)
end_date = datetime.date(2017, 1, 1)

time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
random_date = start_date + datetime.timedelta(days=random_number_of_days)

florg=("on this date: %s\n i met a %s" % (random_date, generate_slug(2)))
print(florg)
 
img = Image.new('RGB', (640, 480), color = (250,255,124))

fnt = ImageFont.truetype('reqqq.ttf', 38)

d = ImageDraw.Draw(img)
d.text((10,150), "you won't believe me, \n but %s" % florg, font=fnt, fill=(188,62,49))

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H-%M-%S")
filenamez=("%s" % generate_slug(2))
img.save('%s_%s.png' % (filenamez, current_time))
