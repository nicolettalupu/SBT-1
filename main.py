from tkinter import *
from tkinter import Tk, Text, BOTH, W, N, E, S, filedialog
from tkinter.ttk import Frame, Button, Label
import plistlib
import os
import re
import sys

regexes = {
    'open': re.compile('^[ \t]*<(item|custom_item|report|if|then|else|condition)[ \t>]'),
    'close': re.compile('^[ \t]*</(item|custom_item|report|if|then|else|condition)[ \t>]'),
    'description': re.compile('^[ \t]*\w*[ \t]*:[ \t]*[\["\'\w+]'),
}


def display(message, exit=0):

    out = sys.stdout
    if exit > 0:
        out = sys.stderr
    return message.rstrip() + '\n'
    if exit > 0:
        sys.exit(exit)


def parse_audit_file(content=None):
    global regexes

    audit = []
    stack = []
    record = {}

    if content is not None:
        lines = [l.strip() for l in content.split('\n')]
        for n in range(len(lines)):
            if regexes['open'].match(lines[n]):
                finds = regexes['open'].findall(lines[n])
                stack.append(finds[0])
                record = {}
            elif regexes['close'].match(lines[n]):
                finds = regexes['close'].findall(lines[n])
                if len(stack) == 0:
                    msg = 'Ran out of stack closing tag: {} (line {})'
                    display(msg.format(finds[0], n), exit=1)
                elif finds[0] == stack[-1]:
                    stack = stack[:-1]
                else:
                    msg = 'Unbalanced tag: {} - {} (line {})'
                    display(msg.format(stack[-1], finds[0], n), exit=2)
                if len(record) != 0:
                    audit.append(record)
                record = {}
            elif regexes['description'].match(lines[n]):
                desc = lines[n].split(':')[1:]
                description = ""
                for d in desc:
                    description += d
                key = "".join(lines[n].split(':')[0:1]).strip()
                record[key] = description
    return audit

class SecurityBenchmarkingTool(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.master.title("Security Benchmarking Tool")
        self.pack(fill=BOTH, expand=True)
       
        self.entry_value = StringVar()
        self.entry_value.trace('w', self.showSearchResults)

        self.columnconfigure((1, 3), weight=1)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(5, weight=1)

        search_label = Label(self)
        search_label.grid(sticky=N + E, row=0, column=0, padx=10, pady=6)

        self.searchEntry = Entry(self, textvariable=self.entry_value)
        self.searchEntry.grid(sticky=E + W + S + N, row=0, column=0, columnspan=4, pady=4)

        open_button = Button(self, text="Open file", command=self.openFile)
        open_button.grid(sticky=S, row=6, column=0, pady=6, padx=70)

        save_button = Button(self, text="Export", command=self.saveFile)
        save_button.grid(sticky=S, row=7, column=0, pady=6, padx=70)

        select_all_button = Button(self, text="Select all options", command=self.selectAll)
        select_all_button.grid(sticky=S, row=6, column=2, pady=6)
        
        enforce_button = Button(self, text="Enforce", command=self.enforce)
        enforce_button.grid(sticky=S, row=7, column=1, pady=6)

        deselect_all_button = Button(self, text="Remove selections", command=self.deselectAll)
        deselect_all_button.grid(sticky=S, row=7, column=2, pady=6)

        test_button = Button(self, text="Test", command=self.openNewWindow)
        test_button.grid(sticky=S, row=6, column=1, pady=6)

        self.list = Listbox(self, selectmode='extended')
        self.list.grid(row=1, column=0, columnspan=5, rowspan=5, sticky=E + W + S + N)
        self.list.config(width=0, height=0)

        self.scrollbar = Scrollbar(self)
        self.list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.list.yview)
        self.scrollbar.grid(column=5, row=1, rowspan=4, sticky=N + S + W)

        self.listContent = list()

    def openNewWindow(self):

        newWindow = Toplevel(self)
        newWindow.title("Test")
        newWindow.geometry("400x400")

        newWindow.columnconfigure(1, weight=1)
        newWindow.rowconfigure(1, weight=1)

        a_file = open("test.txt", "w")
    
        for i in self.list.curselection():
            try:
                    z = (item_type[i])[1:]

                
                    if z == 'CMD_EXEC':
                                info = (output[i])[2:-1]
                                print(i + 1, ')', info, file=a_file)
                                print('Not implemented yet.\n', file=a_file)

                            
                    if z == 'FILECHECK':
                                info = (output[i])[2:-1]
                                print(i + 1, ')', info, file=a_file)
                                print('Not implemented yet.\n', file=a_file)

                            
                    if z == 'FILE_CONTENT_CHECK':
                                info = (output[i])[2:-1]
                                print(i + 1, ')', info, file=a_file)
                                print('Not implemented yet.\n', file=a_file)

                    
                    if z == 'FILE_CONTENT_CHECK_NOT':
                                info = (output[i])[2:-1]
                                print(i + 1, ')', info, file=a_file)
                                print('Not implemented yet.\n', file=a_file)

            except:
                   print(i + 1, ')', 'Path not found.', file=a_file)
                   print(path, '\n', file=a_file)
                   self.list.itemconfig(i, {'bg': 'light gray'})
                   pass

        a_file.close()

        newWindow.textBox = Text(newWindow)
        newWindow.textBox.grid(row=0, column=0, columnspan=5, rowspan=4, sticky=E + W + S + N)

        newWindow.scrollbar = Scrollbar(newWindow)
        newWindow.textBox.config(yscrollcommand=newWindow.scrollbar.set)
        newWindow.scrollbar.config(command=newWindow.textBox.yview)
        newWindow.scrollbar.grid(column=5, row=0, rowspan=4, sticky=N + S + W)

        with open('test.txt', "r") as f:
            data = f.readlines()
        for x in data:
            newWindow.textBox.insert(END, x)

        self.list.selection_clear(0, END)

    def enforce(self):
  
      newWindow = Toplevel(self)
      newWindow.title("Enforce")
      newWindow.geometry("800x400")

      newWindow.columnconfigure(1, weight=1)
      newWindow.rowconfigure(1, weight=1)

      b_file = open("enforce.txt", "w")
  
      for i in self.list.curselection():
          try:
                  z = (item_type[i])[1:]

              
                  if z == 'CMD_EXEC':
                              info = (output[i])[2:-1]
                              print(i + 1, ')', info, file=b_file)
                              print('Done\n', file=b_file)

                          
                  if z == 'FILECHECK':
                              info = (output[i])[2:-1]
                              print(i + 1, ')', info, file=b_file)
                              print('Done\n', file=b_file)

                          
                  if z == 'FILE_CONTENT_CHECK':
                              info = (output[i])[2:-1]
                              print(i + 1, ')', info, file=b_file)
                              print('Done\n', file=b_file)

                  
                  if z == 'FILE_CONTENT_CHECK_NOT':
                              info = (output[i])[2:-1]
                              print(i + 1, ')', info, file=b_file)
                              print('Done\n', file=b_file)

          except:
                 print(i + 1, ')', 'Path not found.', file=b_file)
                 print(path, '\n', file=b_file)
                 self.list.itemconfig(i, {'bg': 'light gray'})
                 pass

      b_file.close()

      newWindow.textBox = Text(newWindow)
      newWindow.textBox.grid(row=0, column=0, columnspan=5, rowspan=4, sticky=E + W + S + N)

      newWindow.scrollbar = Scrollbar(newWindow)
      newWindow.textBox.config(yscrollcommand=newWindow.scrollbar.set)
      newWindow.scrollbar.config(command=newWindow.textBox.yview)
      newWindow.scrollbar.grid(column=5, row=0, rowspan=4, sticky=N + S + W)

      with open('enforce.txt', "r") as f:
          data = f.readlines()
      for x in data:
          newWindow.textBox.insert(END, x)

      self.list.selection_clear(0, END)
    def selectFailed(self):

        for i in range(len(structure)):
            if self.list.itemcget(i, "background") == "red":
                self.list.select_set(i)



    def showSearchResults(self, *args):
        search = self.entry_value.get()
        self.list.delete(0, END)
        for item in self.listContent:
            if search.lower() in item.lower():
                self.list.insert(END, item)

    def selectAll(self):
        self.list.select_set(0, END)

    def deselectAll(self):
        self.list.selection_clear(0, END)

    def saveFile(self):

        file = filedialog.asksaveasfile(mode="w", filetypes=(("Audit files", "*.audit"), ("All files", "*.*")))

        f = open(file.name, "w")
        for i in self.list.curselection():
            print('<custom_item>', file=f)

            z = (item_type[i])[1:]
            if z == 'MACOSX_DEFAULTS_READ':
                print(' type:', (item_type[i])[1:], file=f)
                print(' description:', (output[i])[1:], file=f)
                print(' value_data:', (val_data[i])[1:], file=f)
                print(' plist_name:', (reg_key[i])[1:], file=f)
    

            if z == 'CMD_EXEC':
                print(' type:', (item_type[i])[1:], file=f)
                print(' description:', (output[i])[1:], file=f)
                print(' value_data:', (val_data[i])[1:], file=f)
                
                
            if z == 'FILE_CHECK':
                print(' type:', (item_type[i])[1:], file=f)
                print(' description:', (output[i])[1:], file=f)
                print(' value_data:', (val_data[i])[1:], file=f)
            
            if z == 'FILE_CONTENT_CHECK':
                print(' type:', (item_type[i])[1:], file=f)
                print(' description:', (output[i])[1:], file=f)
                print(' plist_option:', (val_data[i])[1:], file=f)
            
            if z == 'FILE_CONTENT_CHECK_NOT':
                print(' type:', (item_type[i])[1:], file=f)
                print(' description:', (output[i])[1:], file=f)
                print(' plist_option:', (val_data[i])[1:], file=f)




            print('</custom_item>\n', file=f)

        f.close()

    def openFile(self):
        global output
        output = []
        global item_type
        item_type = []
        global val_data
        val_data = []
        global reg_key
        reg_key = []
        global reg_item
        reg_item = []

        file = filedialog.askopenfile(mode="r", filetypes=(("Audit files", "*.audit"), ("All files", "*.*")))

        if not file:
            return

        if file:
            output = []

        f = open(file.name, "r")

        global structure

        structure = []
        structure = parse_audit_file(f.read())

        structure = structure[3:]

        for struct in structure:
            if 'description' in struct:
                output.append(struct['description'])
            else:
                output.append('Tag (description) does not exist for current item.')

        for struct in structure:
            if 'type' in struct:
                item_type.append(struct['type'])
            else:
                item_type.append('Tag (type) does not exist for current item.')

        for struct in structure:
            if 'plist_option' in struct:
                val_data.append(struct['plist_option'])
            else:
                val_data.append('Tag (plist_option) does not exist for current item.')

        for struct in structure:
            if 'plist_item' in struct:
                reg_key.append(struct['plist_item'])
            else:
                reg_key.append('Tag (plist_item) does not exist for current item.')

        for struct in structure:
            if 'plist_name' in struct:
                reg_item.append(struct['plist_name'])
            else:
                reg_item.append('Tag (plist_name) does not exist for current item.')


        values = StringVar()
        values.set(output)

        form = '{}'

        self.list.delete(0, END)

        for (text) in output:
            self.list.insert(END, form.format(text))

        self.listContent = self.list.get(0, END)

def main():
    root = Tk()
    root.geometry("1400x1400")
    root.option_add('*Self', 'black')
    root.option_add('*Listbox*Background', 'gray')

    app = SecurityBenchmarkingTool()
    root.mainloop()


if __name__ == '__main__':
    main()
