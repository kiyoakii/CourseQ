<template>
  <div id="calendar">
    <!-- year + month -->
    <div id="title">
      <ul>
        <li class="arrow" @click="pickPre(currentYear,currentMonth)">
          ＜
        </li>
        <li id="yearmonth" @click="pickYear(currentYear,currentMonth)">
          <span id="year">
            {{currentYear}} 年
          </span>
          <span id="month">
            {{currentMonth}} 月
          </span>
        </li>
        <li class="arrow" @click="pickNext(currentYear,currentMonth)">
          ＞
        </li>
      </ul>
    </div>
    <!-- weeks -->
    <ul id="dayname">
      <li>一</li>
      <li>二</li>
      <li>三</li>
      <li>四</li>
      <li>五</li>
      <li style="color: red">六</li>
      <li style="color: red">日</li>
    </ul>
    <ul class="days">
      <li v-for="dayobject in days" :key="dayobject.day">
        <span class="notcurmonth" v-if="dayobject.day.getMonth()+1 != currentMonth">
          {{dayobject.day.getDate()}}
        </span>
        <span v-else class="normalday">
          {{dayobject.day.getDate()}}
        </span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'CourseCalendar',
  data() {
    return {
      currentDay: 1,
      currentMonth: 1,
      currentYear: 1970,
      currentWeek: 1,
      days: [],
    };
  },
  props: {
    schedule: {
      type: Object,
      default() {
        return {
          month: 4,
          date: 20,
          context: "I'm hungry!",
        };
      },
    },
  },
  created: function init() {
    this.initSchedule(null);
  },
  methods: {
    formatDate(year, month, date) {
      const yearString = year.toString();
      const monthString = (month < 10) ? `0${month}` : `${month}`;
      const dateString = (date < 10) ? `0${date}` : `${date}`;
      return (`${yearString}-${monthString}-${dateString}`);
    },
    initSchedule(time) {
      let date;

      if (time) {
        date = new Date(time);
      } else {
        const now = new Date();
        const d = new Date(this.formatDate(now.getFullYear(), now.getMonth(), 1));
        d.setDate(35);
        date = new Date(this.formatDate(d.getFullYear(), d.getMonth() + 1, 1));
      }
      this.currentDay = date.getDate();
      this.currentYear = date.getFullYear();
      this.currentMonth = date.getMonth() + 1;
      this.currentWeek = date.getDay();
      if (this.currentWeek === 0) {
        this.currentWeek = 7;
      }
      const str = this.formatDate(this.currentYear, this.currentMonth, this.currentDay);
      this.days.length = 0;
      // current week
      for (let i = this.currentWeek - 1; i >= 0; i -= 1) {
        const d = new Date(str);
        d.setDate(d.getDate() - i);
        const dayobject = {}; // 包装Date对象
        dayobject.day = d;
        this.days.push(dayobject); // 日期对象push入days数组中
      }
      // other weeks
      for (let i = 1; i <= 35 - this.currentWeek; i += 1) {
        const d = new Date(str);
        d.setDate(d.getDate() + i);
        const dayobject = {};
        dayobject.day = d;
        this.days.push(dayobject);
      }
    },
    pickPre(year, month) {
      const d = new Date(this.formatDate(year, month, 1));
      d.setDate(0);
      this.initSchedule(this.formatDate(d.getFullYear(), d.getMonth() + 1, 1));
    },
    pickNext(year, month) {
      const d = new Date(this.formatDate(year, month, 1));
      d.setDate(35);
      this.initSchedule(this.formatDate(d.getFullYear(), d.getMonth() + 1, 1));
    },
    pickYear(year, month) {
      // eslint-disable-next-line
      alert(`${year.toString()}-${month.toString()}`);
    },
  },
};
</script>

<style>
* {
  box-sizing: border-box;
}

.ul {
  list-style-type: none;
}

.body {
  font-family: Verdana, sans-serif;
  background: #E8F0F3;
}
#calendar{
  width:100%;
  margin: 0 auto;
  box-shadow: 0 2px 2px 0 rgba(0,0,0,0.14), 0 3px 1px -2px rgba(0,0,0,0.1),
    0 1px 5px 0 rgba(0,0,0,0.12);
}
#title {
  width: 100%;
  background: #00B8EC;
}

#title ul {
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: space-between;
}

#yearmonth {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
}

#yearmonth:hover {
  background: rgba(150, 2, 12, 0.1);
}

#year {
  padding-left: 20px;
  padding-right: 20px;
}

#month {
  text-align: center;
  font-size: 1.5rem;
}

.arrow {
  padding: 30px;
}
.arrow:hover {
  background: rgba(100, 2, 12, 0.1);
}

#title ul li {
  color: white;
  font-size: 20px;
  text-transform: uppercase;
  letter-spacing: 3px;
}

#dayname {
  margin: 0;
  padding: 10px 0;
  background-color: #00B8EC;
  display: flex;
  flex-wrap: wrap;
  color: #FFFFFF;
  justify-content: space-around;
}

#dayname li {
  display: inline-block;
  width: 13.6%;
  text-align: center;
}

.days {
  padding: 0;
  background: #FFFFFF;
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.days li {
  list-style-type: none;
  display: inline-block;
  width: 14.2%;
  text-align: center;
  padding-bottom: 15px;
  padding-top: 15px;
  font-size: 1rem;
  color: #000;
}

.curday {
  padding: 6px 10px;
  border-radius: 50%;
  background: #00B8EC;
  color: #fff;
}

.notcurmonth {
  padding: 5px;
  color: gainsboro;
}

.days li:hover {
  background: #e1e1e1;
}
</style>
