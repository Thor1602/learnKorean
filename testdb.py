from dbHelper import Topics

topic = Topics()
# topic.add_topic(topic="", title="", description="",
#                 rule1="",
#
#                 example1="")

# topic.add_topic(topic="shiot_irregular", title="불규칙 동사 'ㅅ'", description="Irregular verbs with ㅅ",
#                 rule1="We drop ㅅ when a verb stem ends with ㅅ and is followed by a vowel.",
#                 rule2="NOTE: we only apply this rule to the irregular verbs. The verbs need to be studied to know which verb is irregular (like the English irregular verbs.)",
#                 rule3="NOTE: we don't use the rule with the deferential speech level (-습니다, -습니까, etc...)",
#                 example1="Regular: 웃 + 어요 = 웃어요 (smile, laugh)",
#                 example2="Regular: 씻 + 어요 = 씻어요 (wash)",
#                 example3="Irregular 젓 + 어요 = 저어요 (stir)",
#                 example4="Irregular 긋 + 어요 = 그어요 (draw)",
#                 example5="Regular: 벗다(get off), 앗다(exchange), 솟다(rise), 씻다(wash)",
#                 example6="Irregular: 낫다(recover), 긋다(draw), 붓다(swell), 잇다(connect) ")

# topic.add_topic(topic="speech_levels", title="언어 수준", description="Speech Levels",
#                 rule1="1. Like most languages, Korean has different speech levels (-어, -습니다) with different contexts (question, statement).",
#                 rule2="2 .There are basically four speech levels that can be used in four different contexts",
#                 rule3="<strong>Four speech levels: </strong> Deferential, Formal, Informal and Plain.",
#                 rule4="<strong>Four contexts:</strong> Declarative (I go.), Interrogative(Do you go?), Imperative (Go!) and Propositive(Let's go.)",
#                 example1="<h4>동사끝 - Verb Endings</h4>",
#                 example2="""<table class="table">
#   <thead class="thead-dark">
#     <tr>
#       <th scope="col"></th>
#       <th scope="col">Declarative (.)</th>
#       <th scope="col">Interrogative (?)</th>
#       <th scope="col">Imperative (!)</th>
#       <th scope="col">Propositive (.?)</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th scope="row">Deferential</th>
#       <td>-습니다/-ㅂ니다</td>
#       <td>-습니까/-ㅂ니까</td>
#       <td>-(으)십시오</td>
#       <td>-(으)십시다</td>
#     </tr>
#     <tr>
#       <th scope="row">Formal</th>
#       <td>-어요/-아요/-여요</td>
#       <td>-어요/-아요/-여요</td>
#       <td>-(으)세요</td>
#       <td>-어요/-아요/-여요</td>
#     </tr>
#     <tr>
#       <th scope="row">Informal</th>
#       <td>-어/-아/-여</td>
#       <td>-어/-아/-여</td>
#       <td>-어/-아/-여</td>
#       <td>-어/-아/-여</td>
#     </tr>
#         <tr>
#       <th scope="row">Plain</th>
#       <td>-(느)ㄴ다</td>
#       <td>-(으)니/-냐</td>
#       <td>-어라/-아라</td>
#       <td>-자</td>
#     </tr>
#   </tbody>
# </table>""",
# example3="""<table class="table">
#   <thead class="thead-dark">
#     <tr>
#       <th scope="col"></th>
#       <th scope="col">Declarative (.)</th>
#       <th scope="col">Interrogative (?)</th>
#       <th scope="col">Imperative (!)</th>
#       <th scope="col">Propositive (.?)</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th scope="row">Deferential</th>
#       <td>밥을 먹습니다. <br>(I eat a meal.)</td>
#       <td>서울시에 갑니까? <br>(Are you going to Seoul?)</td>
#       <td>정답을 고르십시오! <br>(Please choose the correct answer!)</td>
#       <td>택시를 타십시다. <br>(Let's take a taxi.)</td>
#     </tr>
#     <tr>
#       <th scope="row">Formal</th>
#       <td>한국을 좋아해요. <br>(I like Korea.)</td>
#       <td>소포를 받아요? <br>(Did you receive your parcel?)</td>
#       <td>매일 얼굴을 씻으세요! <br>(Wash your face!)</td>
#       <td>함께 뛰어요. <br>(Let's run together.)</td>
#     </tr>
#     <tr>
#       <th scope="row">Informal</th>
#       <td>엄마 사랑해. <br>(I love you, mommy.)</td>
#       <td>책을 읽어? <br>(Do you read books?)</td>
#       <td>방청소 해! <br>(Clean your room!)</td>
#       <td>우리 같이 요리해. <br>(We are cooking together.)</td>
#     </tr>
#         <tr>
#       <th scope="row">Plain</th>
#       <td>칭구와 운동을 한다. <br>(I exercise with a friend.)</td>
#       <td>어디에 숨었니? <br>(Where did you hide?)</td>
#       <td>숙제를 만들어라! <br>(Do your homework!)</td>
#       <td>노래 부르자. <br>(Let's sing a song.)</td>
#     </tr>
#   </tbody>
# </table>""")

# topic.add_topic(topic="digeut_irregular", title="불규칙 동사 'ㄷ'", description="Irregular verbs with ㄷ",
#                 rule1="We change ㄷ with ㄹ when a verb stem ends with ㄹ and is followed by a vowel.",
#                 rule2="<strong>NOTE:</strong> we only apply this rule to the irregular verbs. The verbs need to be studied to know which verb is irregular.",
#                 rule3="<strong>NOTE:</strong> we don't use the rule with the deferential speech level (-습니다, -습니까, etc...)",
#                 example1="<strong>Regular:</strong> 받 + 아요 = 받아요 (receive)",
#                 example2="<strong>Regular:</strong>  닫+ 아요 = 닫아요 (close)",
#                 example3="<strong>Irregular:</strong> 듣 + 어요 = 들어요 (listen, hear)",
#                 example4="<strong>Irregular:</strong> 묻 + 어요 = 물어요 (ask)",
#                 example5="<strong>Regular:</strong> 믿어요(trust), 얻어요(receive), 쏟아요(pour), 묻어요(ask)",
#                 example6="<strong>Irregular:</strong> 깨달아요(realize), 실어요(load), 걸어요(walk), 물어요(bury)")

# topic.add_topic(topic="bieup_irregular", title="불규칙 동사 'ㅂ'", description="Irregular verbs with 'ㅂ'",
#                 rule1="1 Verbs that end with ㅂ, can have an irregular conjugation.",
#                 rule2="2 If the vowel before ㅂ is 오, you change ㅂ with 오.",
#                 rule3="3 If the vowel before ㅂ is <strong>not</strong> 오, you change ㅂ with 우.",
#                 rule4="<strong>NOTE:</strong> this rule is common, so we apply it to most of the verb endings with ㅂ.",
#                 rule5="<strong>NOTE:</strong> a small part of verbs ending with ㅂ are conjugated like normal verbs.",
#                 rule6="<strong>NOTE:</strong> we don't use the rule with the deferential speech level (-습니다, -습니까, etc...)",
#                 example1="<strong>Regular irregular:</strong> 씹 + 어요 = 씹어요 (bite)",
#                 example2="<strong>Regular irregular:</strong> 입 + 어요 = 입어요 (wear)",
#                 example3="<strong>Regular irregular:</strong> 잡아요(catch), 좁아요(narrow), 넓어요(wide)",
#                 example4="<strong>Irregular:</strong> 눕 + 어요 = 누워요 (lie down)",
#                 example5="<strong>Irregular:</strong> 귀엽 + 어요 = 귀여워요 (cute)",
#                 example6="<strong>Irregular:</strong> 구워요(bake), 더워요(hot), 쉬워요(easy), 아름다워요(beautiful)")
#topic.del_topic('11')
print(topic.check_topic())

