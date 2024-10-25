---
title: Contact
date: 2024-10-24

type: landing

sections:
  - block: contact
    content:
      title: Contact
      text: |-
        竭诚欢迎机械、控制、材料、生物等相关专业的学生报考！


      email: wanghuaping@bit.edu.cn
      phone: 010-68917765
      address:
        street: 北京理工大学中关村校区国防科技园6号楼714
        city: 北京
        region: CN
        country: 中国

      coordinates:
        latitude: '116.31073'
        longitude: '39.95797'
      # directions: Enter Building 1 and take the stairs to Office 200 on Floor 2
      office_hours:
        - '上午：09：00 - 12：00'
        - '下午：14：00 - 18：00'
      # appointment_url: 'https://calendly.com'
      #contact_links:
      #  - icon: comments
      #    icon_pack: fas
      #    name: Discuss on Forum
      #    link: 'https://discourse.gohugo.io'
    
      # Automatically link email and phone or display as text?
      autolink: true
    
      # Email form provider
      form:
        provider: netlify
        formspree:
          id:
        netlify:
          # Enable CAPTCHA challenge to reduce spam?
          captcha: false
    design:
      columns: '1'

  - block: markdown
    content:
      title:
      subtitle: ''
      text:
    design:
      columns: '1'
      background:
        image: 
          filename: contact.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen
---
