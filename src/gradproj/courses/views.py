from django.shortcuts import render


# def java_view(request):
#     context={'':''}
#     context={
#         'description':'',
#         'course_name':'c++',
#         'link':'https://www.youtube.com/embed/?listType=playlist&list=change this'
#
#     }
#     return render(request=request, template_name=r"coursesList.html", context=context)
# Create your views here.
def c_view(request):
    context = {'': ''}
    context = {
        'description': "This course is an introduction to computer programming, and to the C++ programming language. No previous programming experience is required. The course allows students to learn about the language of a computer, and the evolution of programming languages. The course gives an idea about the role of compilers, and examine real c++ programs. Topics will include variable types, operators, control flow, functions, program structure, input and output, arrays, classes. These topics make students familiar with the basic components of a C++ program, including functions, special symbols, and identifiers. During the course, the students will learn Discover how to input data into memory using input statements, and become familiar with the use of increment and decrement operators. Students will learn also about control structures, examine relational and logical operators, and explore how to form and evaluate logical (Boolean) expressions. Thoughout the course, students will explore how to construct and use count-controlled, sentinel-controlled, flag-controlled, and EOFcontrolled repetition structures. In the mean time, they will learn about standard (predefined) functions and discover how to use them in a program, learn about user-defined functions, and examine valuereturning functions, including actual and formal parameters. At the end of this course, students will learn about arrays, explore how to declare and manipulate data into arrays, learn about “array index out of bounds”, and become familiar with the restrictions on array processing.  ",
        'course_name': 'Introduction to Programming',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PL1DUmTEdeA6IUD9Gt5rZlQfbZyAWXd-oD'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def java_view(request):
    context = {'': ''}
    context = {
        'description': 'The course enables you to understand the basic principles of programming. The language used for the course is Java, chosen because it supports object oriented programming and because it is becoming widely used in industry. The course will include discussions and explanations of the following topics: introduction to programming; writing, compiling, and running simple programs; expressions, variables, and assignments; control structures; objects and classes, methods, and arrays.',
        'course_name': 'Object Oriented Programming (1)',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PL1DUmTEdeA6Icttz-O9C3RPRF8R8Px5vk'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def ds_view(request):
    context = {'': ''}
    context = {
        'description': 'Presents fundamental techniques in the design and analysis of data'
                       'structures that lie at the heart of computer science (e.g. data structures'
                       'include: lists, stacks, queues, trees, priority queues, hashing, graphs, and'
                       'search trees). Introduces algorithm design and analysis techniques such as'
                       'recursion and formal methods for analyzing the time and space'
                       'requirements of programs. Provide programming assignments that require'
                       'students to apply the concepts introduced in classes in the development of'
                       'rather large programs. Demonstrate awareness of current areas of research'
                       'by locating and summarizing examples of recent progress.',
        'course_name': 'Data Structures',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PLE_E4BccYnp3vpaLpNTQYZYvdxZViD0vs'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def vs_view(request):
    context = {'': ''}
    context = {
        'description': 'This course is designed for second year undergraduate students to provide them an introduction to the principles of programming for Windows in Visual Basic. The course introduce event driven programming and several popular visual interface controls, data types, control structures, properties, events, modular programming and accessing Database with ADO.net',
        'course_name': 'Visual Basic',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PLdUHNiwJgn86zVowX6MklKqa2_6SnY1CX'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def swe_view(request):
    context = {'': ''}
    context = {
        'description': 'This course covers the software development process, from requirements elicitation and analysis, through specification and design, to implementation, integration, testing, and maintenance (evolution). A variety of concepts, principles, techniques, and tools are presented, encompassing topics such as software processes, software requirements, system models, architectural design, user interface design, verification and validation, and software evolution. ',
        'course_name': 'Software Engineering ',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PL08ef9eJxtJZvt5BOsT46vN6kWnflVKH4'
    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def java2_view(request):
    context = {'': ''}
    context = {
        'description': 'Continuation of Object Oriented Programming (1). Introduces more'
                        'advanced elements of object-oriented programming in Java, including'
                        'inheritance, polymorphism, abstract classes, interfaces, GUIs, exception'
                        'handling, event driven programming.',
        'course_name': 'Java 2',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PL1DUmTEdeA6Icttz-O9C3RPRF8R8Px5vk'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def web_view(request):
    context = {'': ''}
    context = {
        'description': 'This course is designed for the third and the fourth year undergraduate students. It introduces the required skills to build client-side applicationsusing HTML5, CSS3, JavaScript and server-side programs using php language. It demonestrates how to install the Apache server with the other three packages: phpMyAdmin, MYSQL database manager and the php interpreter. It also demostrate how to host/run web documents and the client-server applications on the Apache server. Besides, it shows how to create a database using phpMyAdmin, how to connect client-server applications to MYSQL database and how to write basic DML statementsin php programs.',
        'course_name': 'Web Programming',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PLVrN2LRb7eT2B6v1EwsCS28QkkDTZ5LRm'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def database_view(request):
    context = {'': ''}
    context = {
        'description': 'Introduction to Database Management Systems will concentrate on the'
                       'principles, design, implementation and applications of database'
                       'management systems. The course aims to provide students with a'
                       'foundation in data management concepts and database systems. It includes'
                       'representing information with the relational database model, manipulating'
                       'data with an interactive query language (SQL) and database programming,'
                       'database development.',
        'course_name': 'Introduction to Database Systems',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PL37D52B7714788190'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def multi_view(request):
    context = {'': ''}
    context = {
        'description': 'This course teaches the concepts and skills of using text, images, sound, animation, and video to create multimedia projects and applications. Students will learn the basic principles of each media type including digital representation and issues that arise when media are combined. Students will deal with ethical and legal issues, design considerations including usability, hardware and software that enable multimedia, data representation and file types, data storage, data transmission, digitizing and compression techniques.',
        'course_name': 'Multi Media programming',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PL2D1Iaei9oS6p-Y83mzmf1dp-SphC4dZM'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def algo_view(request):
    context = {'': ''}
    context = {
        'description': 'This course gives a broad introduction to the analysis and design of computer algorithms. '
                       'General topics to be covered include: growth of functions, recurrences, sorting, '
                       'divide-and-conquer, various data structures, dynamic programming, greedy algorithms, '
                       'graph searching and graph algorithms.',
        'course_name': 'Algorithems',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PLAwv14VhKVaa1A6nAaNb7i78t9cFOUwBB'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def DMining_view(request):
    context = {'': ''}
    context = {
        'description': 'Data mining or knowledge discovery from databases (KDD) is one of the most active areas of research in databases. It is at the intersection of database systems, statistics, AI/machine learning, and data visualization. In this course, we will introduce the concepts of data mining and presentdata mining algorithms and applications. Topics include association rule mining, classification models, clustering, data visualization, mining complex types of data (text mining, multimedia mining, Web mining), data mining languages, data mining applications and new trends. The practical part includes applications and exercises using a data mining tool such as WEKA',
        'course_name': 'Data Mining',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PLAZCf_VoDEsNLibPBaqkSYswfETbyyCnH'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def ai_view(request):
    context = {'': ''}
    context = {
        'description': '',
        'course_name': 'Artificial Intilligance',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PLMm8EjqH1EFVR5O5wZCAy9x9mautNuxI6'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def secure_view(request):
    context = {'': ''}
    context = {
        'description': 'This course is designed for second year undergraduate students and it is a comprehensive study of the principles and practices of computer system security including , the OSI security architecture, security attacks, security mechanisms, symmetric ciphers, Classical encryption techniques, data encryption standards (DES), primary numbers, introduction to number theory, public-key cryptosystems, RSA algorithm, message authentication, digital signature, Hash function.',
        'course_name': 'Information Systems Security',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PLd2pEan0ZG_Y1lTa4mXV1y0h-iJjINrqX'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def analysis_view(request):
    context = {'': ''}
    context = {
        'description': 'This course is designed for second year undergraduate students to provide them with a methodical approach to develop computer information systems of different types such as transaction processing systems, decision support systems, knowledge management systems, learning management systems and database management systems. The approach includes systems planning, analysis, design, and implementation and emphases on the strategies and techniques of systems analysis and design for producing logical methodologies for dealing with complexity in the development of information systems. It addresses a wide range of topics starting from the role of the systems analyst, setting Information System (IS) project goals, developing work plans and methods to achieve those goals, measuring progress against a project plan, feasibility study of IS project, models of software development, determining system requirements (functional and non-functional requirements), structuring the requirements (process, logic and data) and ending with designing the database for the proposed project. A project is given to all students that should cover analysis and design phases of a business case; with emphasis on process modeling (DFDs) and data modeling (ER diagrams).',
        'course_name': 'Analysis',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PLMzaNeHCFdm-0QIV9CuFZpIi_4-nKH4Xi'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def disc_view(request):
    context = {'': ''}
    context = {
        'description': '',
        'course_name': 'Discrete Mathmatics',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PLxIvc-MGOs6gZlMVYOOEtUHJmfUquCjwz'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def theory_view(request):
    context = {'': ''}
    context = {
        'description': '',
        'course_name': 'Theory of computation',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PLrCBCI_Do84iJ-kiE1F2trKik2Ts4XelM'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def logic_view(request):
    context = {'': ''}
    context = {
        'description': 'This course the following topics are introduced. Digital and numbering systems: conversion methods, binary and complement arithmetic; Boolean algebra; Circuit minimization techniques; Combinational circuits: Adders, Decoders, Encoders, Code Converters; Sequential Circuits: flip-flops, counters, registers, synchronous sequential circuits.',
        'course_name': 'Logic Design',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PLAwv14VhKVabiV420DERMddTzzFiivcTb'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def os_view(request):
    context = {'': ''}
    context = {
        'description': '',
        'course_name': 'Operating Systems ',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PLxIvc-MGOs6ib0oK1z9C46DeKd9rRcSMY'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def org_view(request):
    context = {'': ''}
    context = {
        'description': '',
        'course_name': 'Computer Organization ',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PLezmjxnkHWaq_kgkoQXGU7vdCr9dgJ0B0'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def arch_view(request):
    context = {'': ''}
    context = {
        'description': '',
        'course_name': 'Computer architecture',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PLfhnBieD_d5W2GEdmUdNcbgohuFhceDI4'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def network_view(request):
    context = {'': ''}
    context = {
        'description': 'This course is designed for second year undergraduate students and it is a comprehensive study of the principles and practices of computer system security including , the OSI security architecture, security attacks, security mechanisms, symmetric ciphers, Classical encryption techniques, data encryption standards (DES), primary numbers, introduction to number theory, public-key cryptosystems, RSA algorithm, message authentication, digital signature, Hash function.',
        'course_name': 'Computer Networks',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PLy_2fgXkPiZuMaG9Jmp8PAwimIumf19hp'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def para_view(request):
    context = {'': ''}
    context = {
        'description': 'This course the following topics are introduced. Digital and numbering systems: conversion methods, binary and complement arithmetic; Boolean algebra; Circuit minimization techniques; Combinational circuits: Adders, Decoders, Encoders, Code Converters; Sequential Circuits: flip-flops, counters, registers, synchronous sequential circuits.',
        'course_name': 'Parallel Programming ',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PLEPx7DrqAqKCtXVlXPHGIB-2LHFEsvT7N'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def wire_view(request):
    context = {'': ''}
    context = {
        'description': '',
        'course_name': 'Wireless Communications and Networks',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PLHKTPL-jkzUrpd1zHEZEIywI5MMtOJX0R'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def calc1_view(request):
    context = {'': ''}
    context = {
        'description': '',
        'course_name': 'Calculus 1',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PLPqfiGFQIuTobnEM_tf-KrOQr6vAuJhjl'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def calc2_view(request):
    context = {'': ''}
    context = {
        'description': '',
        'course_name': 'Calculus 2',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PLPqfiGFQIuTqPGdinOK6_ut9LNBU1Fle-'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def phys1_view(request):
    context = {'': ''}
    context = {
        'description': 'Physics 1 is an algebra-based, introductory college-level physics course. Students cultivate their understanding of physics through classroom study, in-class activity, and hands-on, inquiry-based laboratory work as they explore concepts like systems, fields, force interactions, change, conservation, and waves',
        'course_name': 'Physics 101 ',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PLxAmLxkixn_mm9S-TfXUsUJrjYniXwY9p'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def phys2_view(request):
    context = {'': ''}
    context = {
        'description': '',
        'course_name': 'Physics 102',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PLUS1S_3IWfp71FOszxS1jzWNmD9nzuFCU'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)

    def linear_view(request):
        context = {'': ''}
        context = {
            'description': '',
            'course_name': 'Linear Algebra',
            'link': 'https://www.youtube.com/embed/?listType=playlist&list=PLvuToPs04FnD1lFBolGr4ROQaxQ_zyC1c'

        }

    return render(request=request, template_name=r"coursesList.html", context=context)


def nume_view(request):
    context = {'': ''}
    context = {
        'description': '',
        'course_name': 'Numerical',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PLPn4eVPZKtrIFbHPmH5j81H6hcAiw5bKb'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)


def statistics_view(request):
    context = {'': ''}
    context = {
        'description': '',
        'course_name': 'statistics',
        'link': 'https://www.youtube.com/embed/?listType=playlist&list=PLPn4eVPZKtrJCtXn-FeI2_R6bqd6DNlpY'

    }
    return render(request=request, template_name=r"coursesList.html", context=context)
