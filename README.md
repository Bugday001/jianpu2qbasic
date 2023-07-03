# 简谱转qbasic

- 简谱记录方式：
    数字还是数字                               用map替换
    下划线: 用小括号(八分音符)(记在数字前)       字母后加几分的数字
    点:低八度:, 高八度用:' (记在数字前)         用O加数字表示取0到六默认为4
    小节间以 | 划分
    #: 升半个                                  #号
[qbasic格式](https://www.cnblogs.com/djcsch2001/articles/1965318.html)

## Example
两只老虎：  "1231|1231|345-|345-|(5654)31|(5654)31|2,51-|2,51-|"
    -->    "CDEC CDEC EFGP4 EFGP4 G8A8G8F8EC G8A8G8F8EC DO3GO4CP4 DO3GO4CP4"

致爱丽丝：
('3'#2)|('3'#2)('37)(#'2'1)|6(0136)|7(03)(#57)|'1-('3#'2)|('3'#2)('37)(#'2'1)|6(0136)|7(03)('17)|6(07)('1'2)|'3(05)('4'3)|'2(04)('3'2)|'1(03)('2'1)|7---|

"O5E8O4O5D#8O4 O5E8O4O5D#8O4O5E8O4B8O5D#8O4O5C8O4 AP4C8E8A8 BP4E8G#8B8 O5CO4P4O5E8O4O5D#8O4 O5E8O4O5D#8O4O5E8O4B8O5D#8O4O5C8O4 AP4C8E8A8 BP4E8O5C8O4B8 AP4B8O5C8O4O5D8O4 O5EO4P4G8O5F8O4O5E8O4 O5DO4P4F8O5E8O4O5D8O4 O5CO4P4E8O5D8O4O5C8O4 BP4P4P4"