print("hi")
p=input().split('-')
n=input()
g=input().upper()
d=input()
a=f"""
            {d} juin - Groupe {g}<br>
            <input type="radio" name="{n}" value="{p[0]}">
            <label for="{p[0]}">{p[0]}</label><br>
            <input type="radio" name="{n}" value="{p[1]}">
            <label for="{p[1]}">{p[1]}</label><br>
            <input type="radio" name="{n}" value="Egal">
            <label for="eg">Égalité</label>
            <br><br>"""
print(a)