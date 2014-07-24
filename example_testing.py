text = """
[caption id="attachment_2194" align="aligncenter" width="477" caption="You know how we do!"]<a href="http://www.2buntu.com/wp-content/uploads/2011/11/Jesus-Or-Bust-Studio-Believer_0102.png">[image:Jesus-Or-Bust-Studio-Believer_0102.png]</a>[/caption] <h1><strong>Pump of the volume!</strong></h1> Now, this post is long overdue. I've had it in drafts for a while - but I never got around to writing it, and after using this piece of sweetness one more time, I just had to do it man, I had to do it!

[caption id="attachment_2192" align="aligncenter" width="477" caption="I told you man, I told you"]<a href="http://www.2buntu.com/wp-content/uploads/2011/11/Jesus-Or-Bust-Studio-Believer_011.png">[image:Jesus-Or-Bust-Studio-Believer_011.png]</a>[/caption]

If you have never used, or heard of Decibel 2 before, then you have no clue what you are missing. It is an actively developed, feature-filled, yet minimalistic music player. It does what it says on the tin, and then some. Have you ever heard of a media player with a built in terminal? No, you probably haven't. Well guess what. This has one, and it works. I mean, sudo and all. I just added a PPA with it (before writing this).

[caption id="attachment_2196" align="aligncenter" width="477" caption="Yes, it happened."]<a href="http://www.2buntu.com/wp-content/uploads/2011/11/Jesus-Or-Bust-Studio-Believer_0121.png">[image:Jesus-Or-Bust-Studio-Believer_0121.png]</a>[/caption]

In the spirit of minimalism, I'll stop here :). <h1>How do I get it?</h1> Here: <a href="http://gnomefiles.org/content/show.php/Decibel2+Audio+Player?content=146695&amp;PHPSESSID=97f49c52abf4f61d42ede759615eecf4" target="_blank"><em><strong>link</strong></em></a>. I've asked the author if he will add it to his PPA, still waiting for an answer.

[caption id="attachment_2197" align="aligncenter" width="477" caption="I told you man!"]<a href="http://www.2buntu.com/wp-content/uploads/2011/11/Jesus-Or-Bust-Studio-Believer_013.png">[image:Jesus-Or-Bust-Studio-Believer_013.png]</a>[/caption]
"""
text2="""
Folks,

I am your Linux Advocate, Dietrich T. Schmitz.

[caption id="attachment_2931" align="alignright" width="180" caption="Apple Flashback"]<a href="http:/a/2buntu.com/wp-content/uploads/2012/04/apple.jpeg">[image:apple.jpeg]</a>[/caption]

Perhaps, you have read the latest story about the growing <a title="PC World Apple Flashback Attack Story" href="http://www.pcworld.com/businesscenter/article/253403/mac_malware_outbreak_is_bigger_than_conficker.html#tk.rss_news" target="_blank">FlashBack</a> epidemic that attacks Apple OSX-based computers. The media is reporting that this scourge may exceed numbers seen with the <a title="Care for a Conficker?  They're Yummy!" href="http://en.wikipedia.org/wiki/Conficker" target="_blank">Conficker</a> attack on Windows PCs.

If you have Linux, you can do a few things which will keep 'bad things from happening', including the above types of exploits attacking your PC.

Let me be clear here. <strong>Linux can get infected</strong>. But, if you follow a few simple rules, it will never happen:
<ol>
	<li>Obtain your software from the <a title="Repository" href="http://en.wikipedia.org/wiki/Software_repository" target="_blank">GPG key-ring protected repository</a> (repo) for your <a title="Linux Distribution" href="http://en.wikipedia.org/wiki/Linux_distribution" target="_blank">Distribution</a> (Distro),</li>
	<li>If you must go outside your repo, be sure to check the executable with the site's MD5 or preferably SHA <a title="Checksum" href="http://en.wikipedia.org/wiki/Checksum" target="_blank">checksum</a>, and,</li>
	<li>Sandbox your browser App, whatever it is using <a title="Linux Security Modules (LSM)" href="http://en.wikipedia.org/wiki/Linux_security_modules" target="_blank">Linux Security Modules</a>, e.g., SELinux or <a title="Ubuntu AppArmor LSM" href="https://wiki.ubuntu.com/AppArmor" target="_blank">AppArmor</a></li>
</ol>
<em>Ubuntu Linux</em> comes equipped with /etc/apparmor.d/usr.bin.firefox profile, but is 'disabled' out of the box.
You can enable it by first removing the disabled link:
<strong>$sudo rm /etc/apparmor.d/disable/usr.bin.firefox</strong>

then, add the Firefox profile to AppArmor with:
<strong>$sudo apparmor_parser -a /etc/apparmor.d/usr.bin.firefox</strong>

Essentially, everything you do during your Firefox session will be checked by LSM AppArmor using the above enabled profile.<strong> Any exploit which attempts to spawn and escalate privilege level will be</strong> <strong>stopped cold</strong>.

Unlike Windows and Apple, there is no need to scramble on a 'Zero Day' announcement. Your Distro will patch any security vulnerability/exploit affected software application in days if not hours and automatically download to your system.

That's it!

You should be fine. Here's my AppArmor status report:
<pre>dietrich@AOD260:~$ sudo aa-status
[sudo] password for dietrich:
apparmor module is loaded.
14 profiles are loaded.
14 profiles are in enforce mode.
/sbin/dhclient
/usr/lib/NetworkManager/nm-dhcp-client.action
/usr/lib/connman/scripts/dhclient-script
/usr/lib/cups/backend/cups-pdf
/usr/lib/firefox/firefox{,*[^s][^h]}
/usr/lib/firefox/firefox{,*[^s][^h]}//browser_java
/usr/lib/firefox/firefox{,*[^s][^h]}//browser_openjdk
/usr/lib/firefox/firefox{,*[^s][^h]}//sanitized_helper
/usr/lib/telepathy/mission-control-5
/usr/lib/telepathy/telepathy-*
/usr/sbin/cupsd
/usr/sbin/mysqld-akonadi
/usr/sbin/mysqld-akonadi///usr/sbin/mysqld
/usr/sbin/tcpdump
0 profiles are in complain mode.
8 processes have profiles defined.
8 processes are in enforce mode.
/sbin/dhclient (1905)
/usr/lib/firefox/firefox{,*[^s][^h]} (2380)
/usr/lib/firefox/firefox{,*[^s][^h]} (2444)
/usr/lib/firefox/firefox{,*[^s][^h]} (2447)
/usr/lib/firefox/firefox{,*[^s][^h]} (2448)
/usr/lib/firefox/firefox{,*[^s][^h]} (2547)
/usr/lib/telepathy/mission-control-5 (2167)
/usr/sbin/cupsd (1198)
0 processes are in complain mode.
0 processes are unconfined but have a profile defined.
dietrich@AOD260:~$</pre>
Linux with LSM: The safest operating system on the Planet.

I stake my reputation on it.

Dietrich T. Schmitz

Linux Advocate, Human Being
"""
text3="""
<em>[important]I've been to the land of elementary OS, if I remember correctly I download an ISO back when Jupiter came out, but that time I only ran it on a virtual machine. Now, I've been running it on top of my Ubuntu 12.04 Desktop (the software components) on bare metal... and I'm learning to love it ;). With that said, you could say, I'm a wee bit biased, but as always, I will try to be fair to any competition.[/important]</em>

[notice]<strong>Disclaimer:</strong>

This is <strong>not</strong> an anti-gnome rant - but rather just an examination of the current situation and a possible alternative. You be the judge of which is better.[/notice]

[caption id="" align="aligncenter" width="454" caption="About Switchboard 0.9"]<img src="http://i.imgur.com/3h56B.png" />[/caption]

At UDS-P, the idea of greater collaboration between the elementary and Ubuntu communities/developers was discussed. Not only does elementary have apps we could do with, but elementary has some of the <em><strong>ideas</strong></em> that we need, and we have some of the infrastructure and discipline (yes, I know that's a controversial statement. bite me.) that they need.

&nbsp;
<h2>What is Switchboard anyway?</h2>
<em><strong>Switchboard is described as a:</strong></em>
<blockquote>"Modular desktop settings hub"</blockquote>
So essentially then, it is a cup holder for system settings. According to Cassidy James, Community Manager for the <a href="http://elementaryos.org/" target="_blank">elementary OS</a>, <em>anything</em> <a href="https://plus.google.com/108901876667002638432/posts/Wwq66ELYMQP" target="_blank">can be embedded</a> in Switchboard. That includes the funky settings application MyUnity (which is written in GAMBAS, of all things), and Ubuntu One's new (and controversial) Qt interface. It does not control any settings directly itself, so it is lightweight and simple.

Written in Vala, Switchboard also (obviously) is a GTK+ application, and won't draw the usual barrage of (idiotic) condemnation for being written in or using something other than C and GTK+ ;) (fanatics I'm looking at you ?).
<h2>Aight, so what can Switchboard do for me?</h2>
Eh... you?

Anyways... all jokes aside, really, what can Switchboard do for Ubuntu, or for any other Linux OS? Let's take a look at the current situation. We're not going to look into KDE, XFCE, or Enlightenment, since we are dealing with what is shipped with Ubuntu proper. Also, in the case of Gnome, the system settings aren't really broken, it's just that there are some short comings.
<h3>C or a .desktop file, nothing more?</h3>
Pretty much. That's all you can put in Gnome's new Control Center. Now, this is fine, if you are Gnome itself, because you would only have to concern yourself with the settings relevant to Gnome, and not really have to care about third parties (even though you should care about 3rd parties, but that's another story for another post). Of course, the level of integration offered by the current Control Center is commendable. However, the restriction of only allowing hard-coded panels written in C is not very flexible especially when one considers that Ubuntu has a myriad of applications that could put their settings there, but can't be embedded because the developers don't code in C, or don't want to shock users with bad design.

You see, if a setting is not directly integrated into the Control Center's all-in approach, it has to go in via a .desktop file, and that basically means you'll end up with extra windows popping up that are not really connected to the Control Centre. An example of this is the Ubuntu One Control Panel. It has never been integrated, and now to make matters worse, it's written in Qt, and even less visually integrated than before.
<div class="mceTemp mceIEcenter">

[caption id="attachment_2697" align="aligncenter" width="700" caption="Y U NO INTEGRATE?!ONE!?!"]<a href="http://www.2buntu.com/wp-content/uploads/2012/03/Screenshot-from-2012-03-14-1301081.png">[image:Screenshot-from-2012-03-14-1301081.png]</a>[/caption]

</div>
This is also the case with Printer settings, MyUnity, and Language Support settings. Terrible!

Okay, not terrible, but we could be doing a lot better. One of the things that still bugs me on the Linux Desktop is the level of fragmentation even within individual desktop environments. Users should not have to know, or care, whether an application is written in C++ or Erlang, or whether it uses GTK, Qt or EFL - it should <strong>just work</strong> from the standpoint of the user. This is one of the things that has helped Macintosh to succeed where it has - among a market of users who to a large extent don't care what they're running.
<h3>Okay so, what difference does Switchboard make in the big picture?</h3>
<em>Glad, you, or I, asked.</em>

The benefit of using a "container" like Switchboard is that much of the apparent fragmentation can be done away with quite easily. When I used Pantheon, I found it pleasantly surprising just how much the system seems to be trying to hide the fact that its made from many little pieces. Truth be told, you can feel this way on just about any system - until you begin to dig deeper. The system settings make up a large part of a user's perception of the system. After figuring out how to use the system, the next thing most people want to know is how to change things. Let's see how this area of using the desktop can affect user perception:
<ul>
	<li>When everything appears to be tightly integrated, it gives the user a sense that of a stable environment. This is one area where Enlightenment can seem confusing, while KDE seems like a professional system, for example.</li>
	<li>Having to deal with multiple windows is distracting. Distraction leads to frustration. Frustration leads to dissatisfaction.</li>
	<li>No matter how fancy your desktop, if configuring it is confusing, users won't like it.</li>
</ul>
<h3>Not convinced. Show me the money.</h3>
[caption id="attachment_2700" align="aligncenter" width="664" caption="Hmm... they look the same?"]<a href="http://www.2buntu.com/wp-content/uploads/2012/03/Screenshot-from-2012-03-14-135605.png"><img src="http://www.2buntu.com/wp-content/uploads/2012/03/Screenshot-from-2012-03-14-135605-1024x577.png" /></a>[/caption]

On the surface, there isn't much of a difference, and unfortunately at this time, some of the features referred to cannot be demonstrated (because for example there is no Ubuntu One plug for Switchboard as yet (it's still in pre-release or "pre-gold standard" development). The two in this screenshot are so similar you probably wouldn't notice that you're dealing with completely different systems...

...and that's part of the benefit. Replacing Gnome-Control-Center with Switchboard would hardly make a splash (in terms of drawbacks). The biggest hurdle would probably be the ethical issue of using a non-gnome application, which would have a backlash because people would complain and gripe about how Ubuntu is always using things without giving back upstream and blablabla yada yada yada. Personally, I beg to differ.

Switchboard supports most of Gnome Control Center's panels/applets, and support for them is improving. This means that for example, there could be remixes of Ubuntu that use either one, and you wouldn't notice the difference. A Gnome Shell remix, as another example, wouldn't require under the hood changes to give a pretty stock Gnome Experience on top of Ubuntu, in terms of system settings integration, because the underlying components would be easy to change around at will.

With all this being said then, there really is nothing holding back Ubuntu from switching to Switchboard (no pun intended) in future releases, so long as Switchboard is feature complete by then and up to the task. It would just be another area where two communities reach across the table and shake hands, and who knows, Gnome might even be able to pick up this tech for themselves ;).

&nbsp;

<em>/rant off</em>
<em>Roland Taylor, signing out.</em>
"""
text4="""
<span id="internal-source-marker_0.40402930050563646" style="font-size: 15px; font-family: Ubuntu; color: #000000; background-color: transparent; font-weight: normal; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline;">Recently, I stumbled across this website </span><a href="http://spreadubuntu.org"><span style="font-size: 15px; font-family: Ubuntu; color: #1155cc; background-color: transparent; font-weight: normal; font-style: normal; font-variant: normal; text-decoration: underline; vertical-align: baseline;">spreadubuntu.org</span></a><span style="font-size: 15px; font-family: Ubuntu; color: #000000; background-color: transparent; font-weight: normal; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline;">. I never heard of this particular site before. At first glance, it looked pretty nice and professional. It had quite a lot of useful resources like redesigned CD covers, presentations, pamphlets, circulars, etc. which should go a long way in promoting Ubuntu itself.</span>

<span style="font-size: 15px; font-family: Ubuntu; color: #000000; background-color: transparent; font-weight: normal; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline;">But, as I browsed more, I quickly realized that it didn? seem to be pretty active and most of the content only covers 10.10 or older. There were very few materials accounting for 11.10 or the upcoming LTS, 12.04. So, I quickly set out to find out whether the project is still alive or is it looking for some love from the community.</span>

<span style="font-size: 15px; font-family: Ubuntu; color: #000000; background-color: transparent; font-weight: normal; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline;">After some digging, I managed to email Rub?Romero Cordero, who is in charge of the Spread Ubuntu project, and he confirmed that the project is not dead. Just a little inactive.</span>

<span style="font-size: 15px; font-family: Ubuntu; color: #000000; background-color: transparent; font-weight: normal; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline;">So, if you are one of those awesome creative persons and have some free time, please do take some time off to visit the site and see how you can contribute to the site itself. May be we can see some awesome presentations outlining the several features of Ubuntu or pamphlets promoting the use of Ubuntu. Whatever it is, I am pretty sure everyone will appreciate your contribution. </span>

<span style="font-size: 15px; font-family: Ubuntu; color: #000000; background-color: transparent; font-weight: normal; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline;">If you want to talk to the people behind this wonderful project, please drop in at #ubuntu-marketing in </span><a href="http://irc.freenode.net"><span style="font-size: 15px; font-family: Ubuntu; color: #1155cc; background-color: transparent; font-weight: normal; font-style: normal; font-variant: normal; text-decoration: underline; vertical-align: baseline;">irc.freenode.net</span></a><span style="font-size: 15px; font-family: Ubuntu; color: #000000; background-color: transparent; font-weight: normal; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline;"> or send them an email at </span><a href="mailto:spreadubuntu@lists.launchpad.net"><span style="font-size: 15px; font-family: Ubuntu; color: #1155cc; background-color: transparent; font-weight: normal; font-style: normal; font-variant: normal; text-decoration: underline; vertical-align: baseline;">spreadubuntu@lists.launchpad.net</span></a><span style="font-size: 15px; font-family: Ubuntu; color: #000000; background-color: transparent; font-weight: normal; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline;"> (You have to be a part of the </span><a href="https://launchpad.net/%7Espreadubuntu"><span style="font-size: 15px; font-family: Ubuntu; color: #1155cc; background-color: transparent; font-weight: normal; font-style: normal; font-variant: normal; text-decoration: underline; vertical-align: baseline;">Spread Ubuntu team</span></a><span style="font-size: 15px; font-family: Ubuntu; color: #000000; background-color: transparent; font-weight: normal; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline;"> on Launchpad to participate in the mailing list though).</span>
"""
from bs4 import BeautifulSoup

def converter_2buntu(text):

	# Returns true if one of the parents of "block" is pre, else returns false
	def find_pre_parent(block):
		parent_array = [];
		if hasattr(block, "parents"):
			for parent in block.parents:
			    if parent is None:
			        pass
			    else:
			        parent_array.append(parent.name)
			if "pre" in parent_array:
				return True
			else:
				return False
		else:
			return False

	
	# Strips the blocks for shortcodes. The act argument takes two values - rt and rm. rt -> returns string to be replaced and the string of entire shortcode [shortcode]....[/shortcode]. rm -> strips the shortcode tags alone and returns the modified text.
	def strip_blocks(block,text,act):
		open_block = '['+block
		close_block = '[/'+block+']'
		a = text.find(open_block)
		if a != -1:
			a_end = text.find(']',a)
			b = text.find(close_block,a_end)
			b_end,out = b+len(close_block), text[a_end+1:b]
			del_string = text[a:b_end]
			if act == "rt":
				return out, del_string
			elif act == "rm":
				result = text.replace(del_string,out)
				return result
			else:
				return False
		else:
			return False
	
	# Modifies x to add markup provided by arguments y1,y2. Type of modification is specified by act - pre(use y1 only before), prepost(use y1 before, y2 after), wrap(use y1 before and after)
	def mod_text(x,y1,y2,act):
		while soup.find_all(x):
			temp = soup.find(x)
			if not find_pre_parent(temp):
				temp.insert_before(y1)
				if act == "wrap":
					temp.insert_after(y1)
				elif act == "prepost":
					temp.insert_after(y2)
				elif act == "pre":
					pass
				else:
					return False
				temp.unwrap()
			else:
				return False

	# Remove caption shortcode
	while strip_blocks('caption',text,"rt"):
		out, del_string = strip_blocks('caption',text,"rt")
		short_soup = BeautifulSoup(out)
		if short_soup.a:
			replace_string = "![image]("+short_soup.a['href']+")"
		elif short_soup.img:
			replace_string = "![image]("+short_soup.img['src']+")"
		out_text = text.replace(del_string, replace_string)
		text = out_text

	# Remove [notice]
	while strip_blocks('notice',text,"rm"):
		res = strip_blocks('notice',text,"rm")
		text = res

	# Remove [important]
	while strip_blocks('important',text,"rm"):
		res = strip_blocks('important',text,"rm")
		text = res

	# Create soup
	soup = BeautifulSoup(text)

	# find images and replace
	while soup.find_all('img'):
		i = soup.img
		if i['alt']:
			i = "!["+i['alt']+"]("+i['src']+")"
		else:
			i = "![image]("+i['src']+")"
		soup.img.insert_before(i)
		soup.img.decompose()

	# link replace
	while soup.find_all('a'):
		a = soup.a
		a = "["+a.string+"]("+a['href']+")"
		soup.a.insert_before(a)
		soup.a.decompose()

	# Remove Center Tags
	mod_text('center','\n','','pre')
	# Remove br Tags
	mod_text('br','\n','','pre')
	# Remove hr Tags
	mod_text('hr','\n---','\n','prepost')
	# Remove p
	mod_text('p','\n','','pre')
	# Remove lists
	mod_text('ol','\n','','pre')
	mod_text('ul','\n','','pre')
	# Add li markdown -
	mod_text('li',' - ','','pre')
	# Add h1-h6 markdown #
	mod_text('h1','\n#','\n','prepost')
	mod_text('h2','\n##','\n','prepost')
	mod_text('h3','\n###','\n','prepost')
	mod_text('h4','\n####','\n','prepost')
	mod_text('h5','\n#####','\n','prepost')
	mod_text('h6','\n######','\n','prepost')
	# Add italics markdown _
	mod_text('em','_','','wrap')
	mod_text('i','_','','wrap')
	# Add bold markdown **
	mod_text('strong','**','','wrap')
	mod_text('b','**','','wrap')
	# Add inline code markdown `
	mod_text('code','`','','wrap')
	# Remove span tags
	mod_text('span','\n','','pre')
	# Remove div tags
	mod_text('div','\n','','pre')

	# pre tag replace
	while soup.find_all('pre'):
		pre_text = soup.pre.string
		pre_lines = pre_text.splitlines()
		pre_lines[0] = "\n\t"+pre_lines[0].expandtabs(4)
		pre_lines[-1] = pre_lines[-1]+"\n"
		pre_text = '\n\t'.join(map(str,pre_lines)).expandtabs(4)
		soup.pre.replace_with(pre_text)
		if soup.find('pre'):
			soup.pre.unwrap()

	
	#Remove the body and html tags that BeautifulSoup adds
	soup.body.unwrap()
	soup.html.unwrap()

	return soup

print converter_2buntu(text)
print converter_2buntu(text2)
print converter_2buntu(text3)
print converter_2buntu(text4)