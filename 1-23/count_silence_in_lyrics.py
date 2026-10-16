# 這是楊承道老師（ctyang@rosa.systems）為中原大學
# 「物件導向程式設計」課程所準備的教材範例。

# 基礎語法：字串可用三引號跨行保存，並用 lower()、split() 與迴圈逐字處理。
# 計算歌詞中「silence」這個單字的出現次數。
# 範例使用小寫文字拆分歌詞後逐字比對。
lyrics = '''Hello darkness, my old friend
I've come to talk with you again
Because a vision softly creeping
Left its seeds while I was sleeping
And the vision that was planted in my brain
Still remains
Within the sound of silence
In restless dreams, I walked alone
Narrow streets of cobblestone
'Neath the halo of a street lamp
I turned my collar to the cold and damp
When my eyes were stabbed by the flash of a neon light
That split the night
And touched the sound of silence
And in the naked light, I saw
Ten thousand people, maybe more
People talking without speaking
People hearing without listening
People writing songs that voices never shared
And no one dared
Disturb the sound of silence
"Fools" said I, "You do not know
Silence like a cancer grows
Hear my words that I might teach you
Take my arms that I might reach you"
But my words, like silent raindrops fell
And echoed in the wells of silence
And the people bowed and prayed
To the neon god they made
And the sign flashed out its warning
In the words that it was forming
Then the sign said, "The words on the prophets are written on the subway walls
In tenement halls"
And whispered in the sound of silence'''

def count_silence(lyrics, word='silence'):
    count = 0
    words = lyrics.lower().split()
    for word in words:
        if word == 'silence':
            count += 1
    return count

print(count_silence(lyrics))