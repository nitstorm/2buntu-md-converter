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