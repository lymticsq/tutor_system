from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
#教师表
class Teacher(models.Model):
    name = models.CharField(max_length=255, verbose_name="姓名")
    gender_choices = (
        (1,"男"),
        (2,"女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别",choices=gender_choices,default="1")
    age = models.IntegerField(verbose_name="年龄",default=0)
    education_choices = (
        (1,"大专"),
        (2,"本科"),
        (3,"研究生"),
        (4,"博士"),
    )
    education = models.SmallIntegerField(verbose_name="学历",choices=education_choices,default="1")
    birthday = models.DateField(verbose_name="出生日期",default="1999-01-01")
    graduate = models.CharField(max_length=100,verbose_name="毕业院校",default="无")
    time = models.CharField(max_length=64,verbose_name="授课时间",null=True,blank=True)
    major = models.CharField(max_length=64,verbose_name="所学专业",default="无")
    experience_choices = (
        (1,"一年以下"),
        (2,"二年"),
        (3,"三年"),
        (4,"四年"),
        (5,"五年"),
        (6,"六年"),
        (7,"七年"),
        (8,"八年"),
        (9,"九年"),
        (10,"十年及以上"),
    )
    experience = models.SmallIntegerField(default=0, verbose_name="教学经验(年)",choices=experience_choices)
    region = models.CharField(max_length=64,verbose_name="所在区域",default="无")
    grade_choices =(
        (1, "小学一年级"),
        (2, "小学二年级"),
        (3, "小学三年级"),
        (4, "小学四年级"),
        (5, "小学五年级"),
        (6, "小学六年级"),
        (7, "初一"),
        (8, "初二"),
        (9, "初三"),
        (10, "高一"),
        (11, "高二"),
        (12, "高三"),
        (13, "大学生"),
    )
    grade = models.SmallIntegerField(verbose_name="可授年级",choices=grade_choices,default="1")
    subject_choices =(
        (1, "语文"),
        (2, "数学"),
        (3, "英语"),
        (4, "物理"),
        (5, "化学"),
        (6, "政治"),
        (7, "历史"),
        (8, "地理"),
        (9, "生物"),
        (10, "考研课程"),
    )
    subject = models.SmallIntegerField(verbose_name="教授科目",choices=subject_choices,default="1")
    fee = models.IntegerField(verbose_name="课时费用",null=True,blank=True)
    method_choices = (
        (1, "一对一家教上门"),
        (2, "一对多家教上门"),
        (3, "机构小班授课"),
        (4, "机构大班授课"),
        (5, "远程网络授课"),
    )
    method = models.SmallIntegerField(verbose_name="授课方式",choices=method_choices,default="1")
    regions = models.CharField(max_length=64,verbose_name="可授课区域",default="无")
    description = models.CharField(max_length=255,verbose_name="简历描述",null=True,blank=True)
    create_time = models.DateTimeField(default=timezone.now, verbose_name="创建时间")

#学生表
class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name="姓名")
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices,default="")
    age = models.SmallIntegerField(default=0, verbose_name="年龄")
    grade_choices = (
        (1, "小学一年级"),
        (2, "小学二年级"),
        (3, "小学三年级"),
        (4, "小学四年级"),
        (5, "小学五年级"),
        (6, "小学六年级"),
        (7, "初一"),
        (8, "初二"),
        (9, "初三"),
        (10, "高一"),
        (11, "高二"),
        (12, "高三"),
        (13, "大学生"),
    )
    grade = models.SmallIntegerField(verbose_name="当前年级", choices=grade_choices,default="")
    subject_choices = (
        (1, "语文"),
        (2, "数学"),
        (3, "英语"),
        (4, "物理"),
        (5, "化学"),
        (6, "政治"),
        (7, "历史"),
        (8, "地理"),
        (9, "生物"),
        (10, "考研课程"),
    )
    subject = models.SmallIntegerField(verbose_name="辅导科目", choices=subject_choices,default="")
    region = models.CharField(max_length=64, verbose_name="所在区域",default="")
    time = models.CharField(max_length=64, verbose_name="授课时间",null=True,blank=True)
    description = models.CharField(max_length=255, verbose_name="学生情况", null=True, blank=True)
    teacher_gender = models.SmallIntegerField(verbose_name="教师性别", choices=gender_choices,default="")
    fee = models.IntegerField(verbose_name="课时费用", null=True, blank=True)
    number = models.IntegerField(verbose_name="授课次数", null=True, blank=True)
    identity = models.CharField(max_length=64,verbose_name="身份要求",null=True,blank=True)
    require = models.CharField(max_length=255, verbose_name="家教要求", null=True, blank=True)
    create_time = models.DateTimeField(default=timezone.now, verbose_name="创建时间")

#用户表
class CustomUser(AbstractUser):
    #自定义扩展用户模型
    role = models.CharField(max_length=20, choices=[('admin', '管理员'), ('teacher', '教师'), ('student', '学生')])

    if role != 'admin':
        role_id = models.IntegerField(null=True, blank=True, verbose_name="教师或学生ID")


# 课程表
class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name="课程名称")
    subject = models.CharField(max_length=100, verbose_name="科目")
    level = models.CharField(max_length=50, verbose_name="级别")
    description = models.CharField(max_length=255, verbose_name="课程说明", null=True, blank=True)
    class_hour = models.IntegerField(verbose_name="课时")
    start_time = models.DateField(verbose_name="开课时间")
    end_time = models.DateField(verbose_name="结课时间")
    create_time = models.DateTimeField(verbose_name="创建时间")


# 课程安排表
class Schedule(models.Model):
    teacher_id = models.IntegerField(verbose_name="教师ID")
    student_id = models.IntegerField(verbose_name="学生ID")
    course_id = models.IntegerField(verbose_name="课程ID")
    location = models.CharField(max_length=100, verbose_name="上课地点")
    start_time = models.DateTimeField(verbose_name="上课时间")
    end_time = models.DateTimeField(verbose_name="结束时间")
    create_time = models.DateTimeField(verbose_name="创建时间")


# 教学资源表
class TeachingResource(models.Model):
    teacher_id = models.IntegerField(verbose_name="教师ID")
    name = models.CharField(max_length=255, verbose_name="资源名称")
    type = models.CharField(max_length=50, verbose_name="资源类型(教材、习题、资源等)")
    path = models.CharField(max_length=255, verbose_name="文件路径")
    create_time = models.DateTimeField(verbose_name="创建时间")


# 评价表
class Rating(models.Model):
    target_id = models.IntegerField(verbose_name="被评价用户ID")
    rating_id = models.IntegerField(verbose_name="评价用户ID")
    rating = models.SmallIntegerField(verbose_name="评分")
    comment = models.TextField(verbose_name="评论内容")
    create_time = models.DateTimeField(verbose_name="创建时间")


# 通知表
class Notification(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="sent_notifications")  # 指定相关联的外键，发送用户ID
    receiver = models.ManyToManyField(CustomUser, related_name="received_notifications")  # 与User表指定多对多的关系(会自动另外生成一个中间表)，接收用户ID
    message = models.TextField(verbose_name="消息内容")
    send_time = models.DateTimeField(verbose_name="发送时间")
    is_read = models.BooleanField(verbose_name="是否已读")