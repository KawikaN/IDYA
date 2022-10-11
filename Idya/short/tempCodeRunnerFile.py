class Phrase:
    def __init__(self, name, key): #everytime we create a object(instance) than things within run
        self.name = name
        self.key = key
        print("Waiting for key presses(press backspace to stop)")
        while(keyboard.is_pressed("backspace") != True): #press backspace to stop the loop
            if(keyboard.is_pressed(self.key)): #could not find a way for it to run 1 check then skip an iteration and run the main loop in the main(vl.py) file
                print(self.name)
                continue
        print("Done with phrases")