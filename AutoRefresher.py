import sublime, sublime_plugin, urllib.request


def plugin_loaded():
	global global_settings
	global_settings = sublime.load_settings('AutoRefresher.sublime-settings')
	#print("Loaded")
	#pass

class AutoRefresher(sublime_plugin.EventListener):

	def on_post_save(self, view):
		#print("Save")
		if(global_settings.get("enabled")):
			resp = urllib.request.urlopen(global_settings.get("url"))
			print("Server response: " + resp.readall().decode('UTF-8'))
