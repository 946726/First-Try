from datetime import datetime
from exts import db


class Doctor(db.Model):
    __tablename__ = 'doctor'
    id = db.Column(db.String(100), primary_key=True, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)


class PatientInfo(db.Model):
    __tablename__ = 'patientinfo'
    id = db.Column(db.String(100), primary_key=True, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    mobile = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(200))
    job = db.Column(db.Integer)
    nation = db.Column(db.String(100))
    marital_status = db.Column(db.Boolean)
    emergencyContact = db.Column(db.String(100))
    createDate = db.Column(db.DateTime, default=datetime.now)
    updateDate = db.Column(db.DateTime, default=datetime.now)


class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.String(100), primary_key=True, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(300), nullable=False)


class LifestyleSatusTable(db.Model):
    __tablename__ = 'Lifestyletatustable'
    id = db.Column(db.String(100), primary_key=True, nullable=False)
    smokingHistory = db.Column(db.Integer)
    dailyCigarettes = db.Column(db.Integer)
    drinkingHistory = db.Column(db.Integer)
    dailyAlcohol = db.Column(db.Integer)
    highIntensityExercise = db.Column(db.boolean)
    highIntensityDaysWeek = db.Column(db.Integer)
    highIntensityExerciseDuration = db.Column(db.Integer)
    moderateIntensityExercise = db.Column(db.boolean)
    moderateIntensityExerciseDaysWeek = db.Column(db.Integer)
    moderateIntensityExerciseDuration = db.Column(db.Integer)
    lowIntensityExercise = db.Column(db.boolean)
    lowIntensityExerciseDaysWeek = db.Column(db.Integer)
    lowIntensityExerciseDuration = db.Column(db.Integer)
    sedentaryHours = db.Column(db.Integer)
    favoriteExerciseTypes = db.Column(db.Integer[3])
    dailyGrains = db.Column(db.Integer)
    dailyMeat = db.Column(db.Integer)
    dailyEggs = db.Column(db.Integer)
    dailyVegetables = db.Column(db.Integer)
    monthlyOilUsage = db.Column(db.Integer)
    monthlySaltUsage = db.Column(db.Integer)
    diningOutRate = db.Column(db.Integer)
    dailySleepDuration = db.Column(db.Integer)
    timeToSleep = db.Column(db.Integer)
    sleepOnsetDifficulty = db.Column(db.Integer)
    earlyAwakening = db.Column(db.Integer)
    nightmareRate = db.Column(db.Integer)
    nocturiaFrequency = db.Column(db.Integer)
    createTime = db.Column(db.DateTime, default=datetime.now)
    updateTime = db.Column(db.DateTime, default=datetime.now)


class DiseaseStatusAssessmentForm(db.Model):
    __tablename__ = 'diseasestatusForm'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    chronicDisease = db.Column(db.Integer[3])
    medicationNames = db.Column(db.String(100))
    medicationDuration = db.Column(db.Integer)
    recentInfectionStatus = db.Column(db.String(100))
    recentJointSurgery = db.Column(db.boolean)
    cardiovascularFamilyHistory = db.Column(db.boolean)
    createTime = db.Column(db.DateTime, default=datetime.now)
    updateTime = db.Column(db.DateTime, default=datetime.now)


class PhysicalInformationForm(db.Model):
    __tablename__ = 'PhysicalInformationForm'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    height = db.Column(db.Double)
    weight = db.Column(db.Double)
    waistline = db.Column(db.Double)
    restingHeartRate = db.Column(db.Integer)
    sbp = db.Column(db.Integer)
    dbp = db.Column(db.Integer)
    updateTime = db.Column(db.DateTime, default=datetime.now)


class BiochemicalIndicatorsInformationForm(db.Model):
    __tablename__ = 'biochemicalIndicatorsInformationForm'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tc = db.Column(db.Double)
    tg = db.Column(db.Double)
    ldl = db.Column(db.Double)
    hdl = db.Column(db.Double)
    fpg = db.Column(db.Double)
    hba1c = db.Column(db.Double)
    scr = db.Column(db.Double)
    alb = db.Column(db.Double)
    ast = db.Column(db.Double)
    alt = db.Column(db.Double)
    sua = db.Column(db.Double)
    updateTime = db.Column(db.DateTime, default=datetime.now)


class CarotidArteryIndexInformationForm(db.Model):
    __tablename__ = 'carotidArteryIndexInformationForm'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    leftImt = db.Column(db.Double)
    rightImt = db.Column(db.Double)
    carotidAtheroscleroticPlaque = db.Column(db.Double)
    updateTime = db.Column(db.DateTime, default=datetime.now)


class ABIIndicatorInformationForm(db.Model):
    __tablename__ = 'abiIndicatorInformationForm'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    leftAbi = db.Column(db.Double)
    rightAbi = db.Column(db.Double)
    updateTime = db.Column(db.DateTime, default=datetime.now)


class LiverIndicatorsInformationForm(db.Model):
    __tablename__ = 'liverIndicatorsInformationForm'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    lfap = db.Column(db.Double)
    lsm = db.Column(db.Double)
    updateTime = db.Column(db.DateTime, default=datetime.now)


class PhysicalPotentialEnergyForm(db.Model):
    __tablename__ = 'physicalPotentialEnergyForm'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    crfTestType = db.Column(db.String(100))
    vo2Max = db.Column(db.Double)
    dhgs = db.Column(db.Double)
    sitUpTest5 = db.Column(db.Integer)
    balanceTest30 = db.Column(db.String(100))
    balanceTest60 = db.Column(db.String(100))
    createTime = db.Column(db.DateTime, default=datetime.now)
    updateTime = db.Column(db.DateTime, default=datetime.now)


class ExercisePrescription(db.Model):
    __tablename__ = 'exercisePrescription'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    myobject = db.Column(db.String(100), nullable=False)
    restingHeartRate = db.Column(db.Integer)
    comorbidities = db.Column(db.String(100))
    aerobicExerciseType = db.Column(db.String(100))
    # aerobicAdaptationPrescription
    # aerobicImprovementPrescription
    # aerobicStablePrescription
    resistanceExerciseType = db.Column(db.String(100))
    coreMusclesInvolved = db.Column(db.String(100))
    # resistanceAdaptationPrescription
    # resistanceImprovementPrescription
    # resistanceStablePrescription
    preparationNote = db.Column(db.String(100))
    antidiabeticDrugNote = db.Column(db.String(100))
    dietNote = db.Column(db.String(100))
    unexpectedEventsNote = db.Column(db.String(100))
    createTime = db.Column(db.DateTime, default=datetime.now)
    updateTime = db.Column(db.DateTime, default=datetime.now)


class AerobicExercisePrescription(db.Model):
    __tablename__ = 'aerobicExercisePrescription'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    startTime = db.Column(db.DateTime, default=datetime.now)
    endTime = db.Column(db.DateTime, default=datetime.now)
    warmUpType = db.Column(db.String(100))
    warmUpDuration = db.Column(db.Integer)
    heartRateLowerLimit = db.Column(db.Integer)
    heartRateUpperLimit = db.Column(db.Integer)
    exerciseDuration = db.Column(db.Integer)
    exerciseFrequency = db.Column(db.Integer)
    coolingDownType = db.Column(db.String(100))
    coolingDownDuration = db.Column(db.Integer)


class ResistanceExercisePrescription(db.Model):
    __tablename__ = 'resistanceExercisePrescription'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    startTime = db.Column(db.DateTime, default=datetime.now)
    endTime = db.Column(db.DateTime, default=datetime.now)
    warmUpType = db.Column(db.String(100))
    warmUpDuration = db.Column(db.Integer)
    exercises = db.Column(db.String(100))
    intensity = db.Column(db.String(100))
    number = db.Column(db.Integer)
    groupNumber = db.Column(db.Integer)
    restTime = db.Column(db.Integer)
    exerciseFrequency = db.Column(db.Integer)
    coolingDownType = db.Column(db.String(100))
    coolingDownDuration = db.Column(db.Integer)
