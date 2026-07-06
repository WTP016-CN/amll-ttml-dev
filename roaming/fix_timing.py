#!/usr/bin/env python3
"""Apply Review 2 timing adjustments to the TTML file."""
import sys

filepath = r'd:\UserData\Desktop\amll-ttml-dev\I Knew It, I Knew You - Taylor Swift (1).ttml'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# === LINE 3 ===
# Pa: begin 00:11.632->00:11.872 (+120ms), end 00:12.317->00:12.142 (-175ms)
# ra: end 00:12.953->00:12.808 (-145ms)
# chutes: end 00:13.613->00:13.328 (-285ms)
content = content.replace(
    '<span begin="00:11.632" end="00:12.317">Pa</span><span begin="00:12.378" end="00:12.953">ra</span><span begin="00:12.953" end="00:13.613">chutes</span>',
    '<span begin="00:11.872" end="00:12.142">Pa</span><span begin="00:12.378" end="00:12.808">ra</span><span begin="00:12.953" end="00:13.328">chutes</span>'
)
# of/being boundary: of end +115ms, being begin +115ms
content = content.replace(
    '<span begin="00:14.380" end="00:14.547">of</span> <span begin="00:14.547" end="00:15.236">being</span>',
    '<span begin="00:14.380" end="00:14.662">of</span> <span begin="00:14.662" end="00:15.236">being</span>'
)
# L3 p begin time
content = content.replace(
    '<p begin="00:11.632" end="00:15.646" ttm:agent="v1" itunes:key="L3">',
    '<p begin="00:11.872" end="00:15.646" ttm:agent="v1" itunes:key="L3">'
)

# === LINE 5 ===
# Line end -300ms, time end -300ms
content = content.replace(
    '<p begin="00:24.832" end="00:26.548" ttm:agent="v1" itunes:key="L5">',
    '<p begin="00:24.832" end="00:26.238" ttm:agent="v1" itunes:key="L5">'
)
content = content.replace(
    '<span begin="00:25.797" end="00:26.548">time</span>',
    '<span begin="00:25.797" end="00:26.238">time</span>'
)

# === LINE 7 ===
# seeing end +120ms, you begin +120ms, to end +110ms, night begin +110ms, night end -405ms
content = content.replace(
    '<span begin="00:32.628" end="00:33.239">seeing</span> <span begin="00:33.239" end="00:33.522">you</span> <span begin="00:33.522" end="00:33.872">to</span><span begin="00:33.872" end="00:35.265">night</span>',
    '<span begin="00:32.628" end="00:33.359">seeing</span> <span begin="00:33.359" end="00:33.522">you</span> <span begin="00:33.522" end="00:33.982">to</span><span begin="00:33.982" end="00:34.860">night</span>'
)
content = content.replace(
    '<p begin="00:32.407" end="00:35.265" ttm:agent="v1" itunes:key="L7">',
    '<p begin="00:32.407" end="00:34.860" ttm:agent="v1" itunes:key="L7">'
)

# === LINE 8 ===
# I end -130ms, re begin -130ms
content = content.replace(
    '<span begin="00:35.465" end="00:35.830">I</span> <span begin="00:35.830" end="00:35.900">re</span>',
    '<span begin="00:35.465" end="00:35.700">I</span> <span begin="00:35.700" end="00:35.900">re</span>'
)

# === LINE 9 ===
# Line begin +130ms, Came begin +130ms
content = content.replace(
    '<p begin="00:37.382" end="00:38.816" ttm:agent="v1" itunes:key="L9">',
    '<p begin="00:37.512" end="00:38.816" ttm:agent="v1" itunes:key="L9">'
)
content = content.replace(
    '<span begin="00:37.382" end="00:37.766">Came</span>',
    '<span begin="00:37.512" end="00:37.766">Came</span>'
)

# === LINE 10 ===
# Line end -100ms, then word-level adjustments
content = content.replace(
    '<p begin="00:38.816" end="00:42.382" ttm:agent="v1" itunes:key="L10">',
    '<p begin="00:38.816" end="00:42.282" ttm:agent="v1" itunes:key="L10">'
)
content = content.replace(
    '<span begin="00:40.270" end="00:40.329">ding</span> <span begin="00:40.329" end="00:40.614">there</span> <span begin="00:40.614" end="00:40.812">in</span> <span begin="00:40.812" end="00:40.964">the</span> <span begin="00:40.964" end="00:41.246">light</span> <span begin="00:41.246" end="00:41.462">of</span> <span begin="00:41.462" end="00:41.614">the</span> <span begin="00:41.614" end="00:42.030">win</span><span begin="00:42.030" end="00:42.382">dow</span>',
    '<span begin="00:40.270" end="00:40.459">ding</span> <span begin="00:40.459" end="00:40.744">there</span> <span begin="00:40.744" end="00:40.927">in</span> <span begin="00:40.927" end="00:40.964">the</span> <span begin="00:40.964" end="00:41.391">light</span> <span begin="00:41.391" end="00:41.607">of</span> <span begin="00:41.607" end="00:41.749">the</span> <span begin="00:41.749" end="00:42.030">win</span><span begin="00:42.030" end="00:42.282">dow</span>'
)

# === LINE 13 ===
# Line begin +115ms, end -185ms, But begin +115ms, you end -185ms
content = content.replace(
    '<p begin="00:45.664" end="00:47.614" ttm:agent="v1" itunes:key="L13">',
    '<p begin="00:45.779" end="00:47.429" ttm:agent="v1" itunes:key="L13">'
)
content = content.replace(
    '<span begin="00:45.664" end="00:45.932">But</span>',
    '<span begin="00:45.779" end="00:45.932">But</span>'
)
content = content.replace(
    '<span begin="00:47.215" end="00:47.614">you</span>',
    '<span begin="00:47.215" end="00:47.429">you</span>'
)

# === LINE 14 ===
# I end +155ms, knew begin +155ms end +115ms, it, begin +115ms, you end -245ms
content = content.replace(
    '<p begin="00:49.682" end="00:51.846" ttm:agent="v1" itunes:key="L14">',
    '<p begin="00:49.682" end="00:51.601" ttm:agent="v1" itunes:key="L14">'
)
content = content.replace(
    '<span begin="00:49.682" end="00:49.994">I</span> <span begin="00:49.994" end="00:50.245">knew</span> <span begin="00:50.245" end="00:50.410">it,</span>',
    '<span begin="00:49.682" end="00:50.149">I</span> <span begin="00:50.149" end="00:50.360">knew</span> <span begin="00:50.360" end="00:50.410">it,</span>'
)
content = content.replace(
    '<span begin="00:51.061" end="00:51.846">you</span>',
    '<span begin="00:51.061" end="00:51.601">you</span>'
)

# === LINE 16 ===
# Line begin +140ms, You begin +140ms end -240ms, did end -295ms, too, end -245ms
content = content.replace(
    '<p begin="00:58.058" end="01:02.162" ttm:agent="v1" itunes:key="L16">',
    '<p begin="00:58.198" end="01:02.162" ttm:agent="v1" itunes:key="L16">'
)
content = content.replace(
    '<span begin="00:58.058" end="00:58.759">You</span> <span begin="00:58.814" end="00:59.426">did</span> <span begin="00:59.474" end="01:00.055">too,</span>',
    '<span begin="00:58.198" end="00:58.519">You</span> <span begin="00:58.814" end="00:59.131">did</span> <span begin="00:59.474" end="00:59.810">too,</span>'
)

# === LINE 17 ===
# I end -185ms
content = content.replace(
    '<span begin="01:02.162" end="01:02.946">I</span>',
    '<span begin="01:02.162" end="01:02.761">I</span>'
)

# === LINE 18 ===
# Line end -115ms, For end -265ms, would end +115ms, be begin +115ms, friend end -115ms
content = content.replace(
    '<p begin="01:07.256" end="01:12.764" ttm:agent="v1" itunes:key="L18">',
    '<p begin="01:07.256" end="01:12.649" ttm:agent="v1" itunes:key="L18">'
)
content = content.replace(
    '<span begin="01:07.256" end="01:07.916">For</span>',
    '<span begin="01:07.256" end="01:07.651">For</span>'
)
content = content.replace(
    '<span begin="01:09.074" end="01:09.223">would</span> <span begin="01:09.223" end="01:09.494">be</span>',
    '<span begin="01:09.074" end="01:09.338">would</span> <span begin="01:09.338" end="01:09.494">be</span>'
)
content = content.replace(
    '<span begin="01:12.025" end="01:12.764">friend</span>',
    '<span begin="01:12.025" end="01:12.649">friend</span>'
)

# === LINE 19 ===
# Line end -145ms, has end +105ms, ways begin +105ms, fe end -145ms
content = content.replace(
    '<p begin="01:13.562" end="01:18.513" ttm:agent="v1" itunes:key="L19">',
    '<p begin="01:13.562" end="01:18.368" ttm:agent="v1" itunes:key="L19">'
)
content = content.replace(
    '<span begin="01:14.225" end="01:14.526">has</span> <span begin="01:14.526" end="01:14.876">ways</span>',
    '<span begin="01:14.225" end="01:14.631">has</span> <span begin="01:14.631" end="01:14.876">ways</span>'
)
content = content.replace(
    '<span begin="01:18.230" end="01:18.513">fe</span>',
    '<span begin="01:18.230" end="01:18.368">fe</span>'
)

# === LINE 20 ===
# Line end -240ms, Hi end -240ms
content = content.replace(
    '<p begin="01:19.046" end="01:21.748" ttm:agent="v1" itunes:key="L20">',
    '<p begin="01:19.046" end="01:21.508" ttm:agent="v1" itunes:key="L20">'
)
content = content.replace(
    '<span begin="01:20.659" end="01:21.748">"Hi"</span>',
    '<span begin="01:20.659" end="01:21.508">"Hi"</span>'
)

# === LINE 22 ===
# Line begin +140ms, Came begin +140ms, back end +105ms, when begin +105ms
content = content.replace(
    '<p begin="01:23.830" end="01:25.258" ttm:agent="v1" itunes:key="L22">',
    '<p begin="01:23.970" end="01:25.258" ttm:agent="v1" itunes:key="L22">'
)
content = content.replace(
    '<span begin="01:23.830" end="01:24.217">Came</span> <span begin="01:24.217" end="01:24.534">back</span> <span begin="01:24.534" end="01:24.734">when</span>',
    '<span begin="01:23.970" end="01:24.217">Came</span> <span begin="01:24.217" end="01:24.639">back</span> <span begin="01:24.639" end="01:24.734">when</span>'
)

# === LINE 23 ===
# saw end +110ms, you, begin +110ms end -150ms
content = content.replace(
    '<span begin="01:25.483" end="01:25.849">saw</span> <span begin="01:25.849" end="01:26.321">you,</span>',
    '<span begin="01:25.483" end="01:25.959">saw</span> <span begin="01:25.959" end="01:26.171">you,</span>'
)

# === LINE 24 ===
# Line end -140ms, smile end -140ms
content = content.replace(
    '<p begin="01:28.784" end="01:30.329" ttm:agent="v1" itunes:key="L24">',
    '<p begin="01:28.784" end="01:30.189" ttm:agent="v1" itunes:key="L24">'
)
content = content.replace(
    '<span begin="01:29.656" end="01:30.329">smile</span>',
    '<span begin="01:29.656" end="01:30.189">smile</span>'
)

# === LINE 26 ===
# Line end -155ms, I end +120ms, knew begin +120ms, you end -155ms
content = content.replace(
    '<p begin="01:32.196" end="01:34.014" ttm:agent="v1" itunes:key="L26">',
    '<p begin="01:32.196" end="01:33.859" ttm:agent="v1" itunes:key="L26">'
)
content = content.replace(
    '<span begin="01:32.417" end="01:32.601">I</span> <span begin="01:32.601" end="01:32.813">knew</span>',
    '<span begin="01:32.417" end="01:32.721">I</span> <span begin="01:32.721" end="01:32.933">knew</span>'
)
content = content.replace(
    '<span begin="01:33.744" end="01:34.014">you</span>',
    '<span begin="01:33.744" end="01:33.859">you</span>'
)

# === LINE 27 ===
# Line end -330ms, I end +125ms, knew(1) begin +125ms, knew(2) end +170ms, you begin +170ms end -330ms
content = content.replace(
    '<p begin="01:37.446" end="01:39.598" ttm:agent="v1" itunes:key="L27">',
    '<p begin="01:37.446" end="01:39.268" ttm:agent="v1" itunes:key="L27">'
)
content = content.replace(
    '<span begin="01:37.446" end="01:37.774">I</span> <span begin="01:37.774" end="01:37.979">knew</span>',
    '<span begin="01:37.446" end="01:37.899">I</span> <span begin="01:37.899" end="01:37.979">knew</span>'
)
content = content.replace(
    '<span begin="01:38.427" end="01:38.678">knew</span> <span begin="01:38.678" end="01:39.598">you</span>',
    '<span begin="01:38.427" end="01:38.848">knew</span> <span begin="01:38.848" end="01:39.268">you</span>'
)

# === LINE 28 ===
# Line begin +145ms end -300ms, I begin +145ms end +150ms, knew begin +150ms, you end -300ms
content = content.replace(
    '<p begin="01:42.527" end="01:44.729" ttm:agent="v1" itunes:key="L28">',
    '<p begin="01:42.672" end="01:44.429" ttm:agent="v1" itunes:key="L28">'
)
content = content.replace(
    '<span begin="01:42.527" end="01:42.890">I</span> <span begin="01:42.890" end="01:43.111">knew</span>',
    '<span begin="01:42.672" end="01:43.040">I</span> <span begin="01:43.040" end="01:43.111">knew</span>'
)
content = content.replace(
    '<span begin="01:44.015" end="01:44.729">you</span>',
    '<span begin="01:44.015" end="01:44.429">you</span>'
)

# === LINE 29 ===
# Line begin +105ms end -125ms, Oh begin +105ms, cried end +110ms, when begin +110ms, bye end -125ms
content = content.replace(
    '<p begin="01:54.853" end="01:59.465" ttm:agent="v1" itunes:key="L29">',
    '<p begin="01:54.958" end="01:59.340" ttm:agent="v1" itunes:key="L29">'
)
content = content.replace(
    '<span begin="01:54.853" end="01:55.165">Oh,</span>',
    '<span begin="01:54.958" end="01:55.165">Oh,</span>'
)
content = content.replace(
    '<span begin="01:56.133" end="01:57.432">cried</span> <span begin="01:57.432" end="01:57.622">when</span>',
    '<span begin="01:56.133" end="01:57.542">cried</span> <span begin="01:57.542" end="01:57.622">when</span>'
)
content = content.replace(
    '<span begin="01:58.616" end="01:59.465">bye</span>',
    '<span begin="01:58.616" end="01:59.340">bye</span>'
)

# === LINE 30 ===
# Line begin +260ms end -275ms, Won begin +260ms, dering end +110ms, if begin +110ms end +145ms,
# I'd begin +145ms end +130ms, made begin +130ms, in end +125ms, my begin +125ms, mind end -275ms
content = content.replace(
    '<p begin="02:00.200" end="02:04.897" ttm:agent="v1" itunes:key="L30">',
    '<p begin="02:00.460" end="02:04.622" ttm:agent="v1" itunes:key="L30">'
)
content = content.replace(
    '<span begin="02:00.200" end="02:00.780">Won</span><span begin="02:00.780" end="02:00.989">dering</span> <span begin="02:00.989" end="02:01.256">if</span> <span begin="02:01.256" end="02:01.608">I\'d</span> <span begin="02:01.608" end="02:01.973">made</span>',
    '<span begin="02:00.460" end="02:00.780">Won</span><span begin="02:00.780" end="02:01.099">dering</span> <span begin="02:01.099" end="02:01.401">if</span> <span begin="02:01.401" end="02:01.738">I\'d</span> <span begin="02:01.738" end="02:01.973">made</span>'
)
content = content.replace(
    '<span begin="02:02.608" end="02:03.256">in</span> <span begin="02:03.256" end="02:03.907">my</span> <span begin="02:03.907" end="02:04.897">mind</span>',
    '<span begin="02:02.608" end="02:03.381">in</span> <span begin="02:03.381" end="02:03.907">my</span> <span begin="02:03.907" end="02:04.622">mind</span>'
)

# === LINE 31 ===
# Line end -230ms, look end -125ms, me begin -125ms, eye end -230ms
content = content.replace(
    '<p begin="02:05.103" end="02:08.398" ttm:agent="v1" itunes:key="L31">',
    '<p begin="02:05.103" end="02:08.168" ttm:agent="v1" itunes:key="L31">'
)
content = content.replace(
    '<span begin="02:05.732" end="02:06.066">look</span> <span begin="02:06.066" end="02:06.298">me</span>',
    '<span begin="02:05.732" end="02:05.941">look</span> <span begin="02:05.941" end="02:06.298">me</span>'
)
content = content.replace(
    '<span begin="02:06.898" end="02:08.398">eye</span>',
    '<span begin="02:06.898" end="02:08.168">eye</span>'
)

# === LINE 33 ===
# Line begin +105ms, Came begin +105ms, back end +105ms, when begin +105ms
content = content.replace(
    '<p begin="02:10.297" end="02:11.642" ttm:agent="v1" itunes:key="L33">',
    '<p begin="02:10.402" end="02:11.642" ttm:agent="v1" itunes:key="L33">'
)
content = content.replace(
    '<span begin="02:10.297" end="02:10.678">Came</span> <span begin="02:10.678" end="02:10.996">back</span> <span begin="02:10.996" end="02:11.161">when</span>',
    '<span begin="02:10.402" end="02:10.678">Came</span> <span begin="02:10.678" end="02:11.101">back</span> <span begin="02:11.101" end="02:11.161">when</span>'
)

# === LINE 34 ===
# I end +150ms, saw begin +150ms, you, end -160ms
content = content.replace(
    '<span begin="02:11.642" end="02:11.849">I</span> <span begin="02:11.849" end="02:12.308">saw</span> <span begin="02:12.308" end="02:12.772">you,</span>',
    '<span begin="02:11.642" end="02:11.999">I</span> <span begin="02:11.999" end="02:12.308">saw</span> <span begin="02:12.308" end="02:12.612">you,</span>'
)

# === LINE 36 ===
# Line begin +175ms end -215ms, Yeah begin +175ms, while end -215ms
content = content.replace(
    '<p begin="02:16.697" end="02:18.497" ttm:agent="v1" itunes:key="L36">',
    '<p begin="02:16.872" end="02:18.282" ttm:agent="v1" itunes:key="L36">'
)
content = content.replace(
    '<span begin="02:16.697" end="02:16.971">Yeah,</span>',
    '<span begin="02:16.872" end="02:16.971">Yeah,</span>'
)
content = content.replace(
    '<span begin="02:17.568" end="02:18.497">while</span>',
    '<span begin="02:17.568" end="02:18.282">while</span>'
)

# === LINE 37 ===
# Line end -190ms, Oh end -190ms
content = content.replace(
    '<p begin="02:18.681" end="02:19.948" ttm:agent="v1" itunes:key="L37">',
    '<p begin="02:18.681" end="02:19.758" ttm:agent="v1" itunes:key="L37">'
)
content = content.replace(
    '<span begin="02:18.681" end="02:19.948">Oh</span>',
    '<span begin="02:18.681" end="02:19.758">Oh</span>'
)

# === LINE 38 ===
# Line end -215ms, that end +125ms, same begin +125ms, smile end -215ms
content = content.replace(
    '<p begin="02:20.313" end="02:21.906" ttm:agent="v1" itunes:key="L38">',
    '<p begin="02:20.313" end="02:21.691" ttm:agent="v1" itunes:key="L38">'
)
content = content.replace(
    '<span begin="02:20.684" end="02:20.916">that</span> <span begin="02:20.916" end="02:21.249">same</span> <span begin="02:21.249" end="02:21.906">smile</span>',
    '<span begin="02:20.684" end="02:21.041">that</span> <span begin="02:21.041" end="02:21.249">same</span> <span begin="02:21.249" end="02:21.691">smile</span>'
)

# === LINE 39 ===
# Line begin +105ms end -190ms, Man all +105ms, it's begin +105ms end +135ms, been begin +135ms, while end -190ms
content = content.replace(
    '<p begin="02:21.906" end="02:24.062" ttm:agent="v1" itunes:key="L39">',
    '<p begin="02:22.011" end="02:23.872" ttm:agent="v1" itunes:key="L39">'
)
content = content.replace(
    '<span begin="02:21.906" end="02:22.087">Man,</span> <span begin="02:22.087" end="02:22.287">it\'s</span> <span begin="02:22.287" end="02:22.554">been</span>',
    '<span begin="02:22.011" end="02:22.192">Man,</span> <span begin="02:22.192" end="02:22.422">it\'s</span> <span begin="02:22.422" end="02:22.554">been</span>'
)
content = content.replace(
    '<span begin="02:22.789" end="02:24.062">while</span>',
    '<span begin="02:22.789" end="02:23.872">while</span>'
)

# === LINE 40 ===
# Line begin +140ms, Wea begin +140ms, ring end +125ms, that begin +125ms end +155ms, same begin +155ms
content = content.replace(
    '<p begin="02:25.430" end="02:26.980" ttm:agent="v1" itunes:key="L40">',
    '<p begin="02:25.570" end="02:26.980" ttm:agent="v1" itunes:key="L40">'
)
content = content.replace(
    '<span begin="02:25.430" end="02:25.730">Wea</span><span begin="02:25.730" end="02:25.777">ring</span> <span begin="02:25.777" end="02:25.993">that</span> <span begin="02:25.993" end="02:26.395">same</span>',
    '<span begin="02:25.570" end="02:25.730">Wea</span><span begin="02:25.730" end="02:25.902">ring</span> <span begin="02:25.902" end="02:26.148">that</span> <span begin="02:26.148" end="02:26.395">same</span>'
)

# === LINE 41 ===
# Line begin +110ms, Man begin +110ms
content = content.replace(
    '<p begin="02:27.080" end="02:28.781" ttm:agent="v1" itunes:key="L41">',
    '<p begin="02:27.190" end="02:28.781" ttm:agent="v1" itunes:key="L41">'
)
content = content.replace(
    '<span begin="02:27.080" end="02:27.315">Man,</span>',
    '<span begin="02:27.190" end="02:27.315">Man,</span>'
)

# === LINE 42 ===
# Line end -205ms, I end +150ms, knew begin +150ms, you end -205ms
content = content.replace(
    '<p begin="02:28.921" end="02:30.846" ttm:agent="v1" itunes:key="L42">',
    '<p begin="02:28.921" end="02:30.641" ttm:agent="v1" itunes:key="L42">'
)
content = content.replace(
    '<span begin="02:29.128" end="02:29.312">I</span> <span begin="02:29.312" end="02:29.552">knew</span>',
    '<span begin="02:29.128" end="02:29.462">I</span> <span begin="02:29.462" end="02:29.552">knew</span>'
)
content = content.replace(
    '<span begin="02:30.380" end="02:30.846">you</span>',
    '<span begin="02:30.380" end="02:30.641">you</span>'
)

# === LINE 43 ===
# Line end -195ms, I end +135ms, knew begin +135ms, you end -195ms
content = content.replace(
    '<p begin="02:34.207" end="02:36.097" ttm:agent="v1" itunes:key="L43">',
    '<p begin="02:34.207" end="02:35.902" ttm:agent="v1" itunes:key="L43">'
)
content = content.replace(
    '<span begin="02:34.207" end="02:34.514">I</span> <span begin="02:34.514" end="02:34.730">knew</span>',
    '<span begin="02:34.207" end="02:34.649">I</span> <span begin="02:34.649" end="02:34.730">knew</span>'
)
content = content.replace(
    '<span begin="02:35.530" end="02:36.097">you</span>',
    '<span begin="02:35.530" end="02:35.902">you</span>'
)

# === LINE 44 ===
# Line end -105ms, smile end -105ms
content = content.replace(
    '<p begin="02:38.396" end="02:40.265" ttm:agent="v1" itunes:key="L44">',
    '<p begin="02:38.396" end="02:40.160" ttm:agent="v1" itunes:key="L44">'
)
content = content.replace(
    '<span begin="02:39.431" end="02:40.265">smile</span>',
    '<span begin="02:39.431" end="02:40.160">smile</span>'
)

# === LINE 45 ===
# Line begin +105ms end -365ms, I begin +105ms end +210ms, knew begin +210ms, you end -365ms
content = content.replace(
    '<p begin="02:41.946" end="02:44.297" ttm:agent="v1" itunes:key="L45">',
    '<p begin="02:42.051" end="02:43.932" ttm:agent="v1" itunes:key="L45">'
)
content = content.replace(
    '<span begin="02:41.946" end="02:42.212">I</span> <span begin="02:42.212" end="02:42.474">knew</span>',
    '<span begin="02:42.051" end="02:42.422">I</span> <span begin="02:42.422" end="02:42.474">knew</span>'
)
content = content.replace(
    '<span begin="02:43.324" end="02:44.297">you</span>',
    '<span begin="02:43.324" end="02:43.932">you</span>'
)

# === LINE 46 ===
# Line begin +195ms end -235ms, I begin +195ms, knew end +200ms, you begin +200ms end -235ms
content = content.replace(
    '<p begin="02:47.014" end="02:48.897" ttm:agent="v1" itunes:key="L46">',
    '<p begin="02:47.209" end="02:48.662" ttm:agent="v1" itunes:key="L46">'
)
content = content.replace(
    '<span begin="02:47.014" end="02:47.478">I</span>',
    '<span begin="02:47.209" end="02:47.478">I</span>'
)
content = content.replace(
    '<span begin="02:48.195" end="02:48.462">knew</span> <span begin="02:48.462" end="02:48.897">you</span>',
    '<span begin="02:48.195" end="02:48.662">knew</span> <span begin="02:48.662" end="02:48.662">you</span>'
)

# === LINE 47 ===
# Line end -220ms, I end +135ms, knew begin +135ms, it end -220ms
content = content.replace(
    '<p begin="02:49.662" end="02:50.732" ttm:agent="v1" itunes:key="L47">',
    '<p begin="02:49.662" end="02:50.512" ttm:agent="v1" itunes:key="L47">'
)
content = content.replace(
    '<span begin="02:49.662" end="02:49.964">I</span> <span begin="02:49.964" end="02:50.255">knew</span> <span begin="02:50.255" end="02:50.732">it</span>',
    '<span begin="02:49.662" end="02:50.099">I</span> <span begin="02:50.099" end="02:50.255">knew</span> <span begin="02:50.255" end="02:50.512">it</span>'
)

# Also update div end time (first occurrence only)
content = content.replace(
    'end="02:50.732"><p begin="00:06',
    'end="02:50.512"><p begin="00:06',
    1
)

# Count changes
diff_chars = sum(1 for a, b in zip(original, content) if a != b)
print(f'Characters changed: {diff_chars}')

# Verify some key changes
checks = [
    ('00:11.872', 'L3 Pa begin'),
    ('00:12.142', 'L3 Pa end'),
    ('00:12.808', 'L3 ra end'),
    ('00:13.328', 'L3 chutes end'),
    ('00:14.662', 'L3 of/being boundary'),
    ('00:26.238', 'L5 end'),
    ('00:33.359', 'L7 seeing end'),
    ('00:34.860', 'L7 night end'),
    ('00:35.700', 'L8 I end'),
    ('00:37.512', 'L9 begin'),
    ('00:42.282', 'L10 end'),
    ('00:45.779', 'L13 begin'),
    ('00:50.149', 'L14 I end'),
    ('00:58.198', 'L16 begin'),
    ('02:50.512', 'L47 end / file end'),
]

for val, desc in checks:
    if val in content:
        print(f'  OK: {desc} = {val}')
    else:
        print(f'  MISSING: {desc} = {val}')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('File written successfully.')
