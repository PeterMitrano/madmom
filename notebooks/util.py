# for having playable audio
# courtesy of: https://stackoverflow.com/questions/33417151/playing-mp3-in-a-folder-with-jupyter-notebooimport os
from IPython.display import display,Audio,HTML
playlist_html=""
audio_html=""
music_dir = u'Music'
count=0
for root, dirs, files in os.walk(music_dir):
    #print 'root: ' + repr(root)
    #print 'dirs: ' + repr(dirs)
    #print 'files: ' + repr(files)
    for file in files:
        if count==0:
            playlist_html = u'''<li class="active"><a href="{0}">{1}</a>
                </li>\n'''.format(os.path.join(root, file), file)
            audio_html = u'''<audio id="audio" preload="auto" tabindex="0" controls="" type="audio/mpeg">
                <source type="audio/mp3" src="{}">Sorry, your browser does not support HTML5 audio.
                </audio>'''.format(os.path.join(root, file))
        else:
            playlist_html +=u'''<li><a href="{0}">{1}</a></li>\n'''.format(os.path.join(root, file), file)
        count += 1

playlist_html = audio_html + u'''\n<ol id="playlist">\n{}</ol>'''.format(playlist_html)
#print playlist_html


playlist_css = """
<style>
#playlist .active a{color:#CC0000;text-decoration:none;}
#playlist li a:hover{text-decoration:none;}
</style>
"""

playlist_js = """
<script>
var audio;
var playlist;
var tracks;
var current;

init();
function init(){
    current = 0;
    audio = $('audio');
    playlist = $('#playlist');
    tracks = playlist.find('li a');
    len = tracks.length - 1;
    audio[0].volume = .10;
    playlist.find('a').click(function(e){
        e.preventDefault();
        link = $(this);
        current = link.parent().index();
        run(link, audio[0]);
    });
    audio[0].addEventListener('ended',function(e){
        current++;
        if(current == len){
            current = 0;
            link = playlist.find('a')[0];
        }else{
            link = playlist.find('a')[current];
        }
        run($(link),audio[0]);
    });
}
function run(link, player){
        player.src = link.attr('href');
        par = link.parent();
        par.addClass('active').siblings().removeClass('active');
        audio[0].load();
        audio[0].play();
}
</script>
"""
display(HTML(playlist_html))
display(HTML(playlist_css))
display(HTML(playlist_js))k
