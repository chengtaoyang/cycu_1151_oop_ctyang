# 這是楊承道老師（ctyang@rosa.systems）為中原大學
# 「物件導向程式設計」課程所準備的教材範例。

# 基礎語法：用字串方法拆分文字、用 for 走訪單字，並以字典記錄各字詞次數。
# 統計歌詞中指定單字的出現次數，並移除單字周圍的標點符號。
# 結果以字典列出各單字的計數。
import string


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


def count_silence(lyrics, words):
    # return the count of specified words in the lyrics in Dictionary form (key: word, value: count)

    count_dict = {word: 0 for word in words}

    lyrics_words = lyrics.lower().split()

    for word in lyrics_words:
        for w in words:
            if word.strip(string.punctuation) == w.lower():
                count_dict[w] += 1
    return count_dict


words = ['silence', 'People', 'In', 'the']

rd = count_silence(lyrics, words)

print(rd)