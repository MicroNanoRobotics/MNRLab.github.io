---
# Leave the homepage title empty to use the site title.
title:
date: 2024-10-24
type: landing

sections:
  - block: slider
    content:
      slides:
        - title: 欢迎访问微纳机器人研究小组
          content: 👋 Welcome to the Micro Nano Robotics Lab...
          align: center
          background:
            image:
              filename: contact.jpg
              filters:
                brightness: 0.7
            position: right
            color: '#666'
        - title: 期刊封面
          content: '本团队的代表性成果发表在国际知名杂志xxxxxxxxx'
          align: left
          background:
            image:
              filename: coders.jpg
              filters:
                brightness: 0.5
            position: center
            color: '#555'
        - title: 期刊封面
          content: '本团队的代表性成果发表在国际知名杂志xxxxxxxxx'
          align: left
          background:
            image:
              filename: cover3.jpg
              filters:
                brightness: 0.5
            position: center
            size: contain
            css_class: fullscreen
            color: '#555'
        - title: 获奖证书
          content: '快来加入我们吧!'
          align: right
          background:
            image:
              filename: welcome.jpg
              filters:
                brightness: 0.5
            position: center
            color: '#333'
          link:
            icon: graduation-cap
            icon_pack: fas
            text: Join Us
            url: contact/
    design:
      slide_width: ''
      is_fullscreen: true
      loop: true
      interval: 2000
---
