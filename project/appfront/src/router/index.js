import Vue from 'vue'
import Router from 'vue-router'
import Index from "./../components/FirstPage/Index.vue";
import Dashboard from "../components/User/Dashboard.vue";
import Dashboard_admin from "../components/admin/Dashboard_admin.vue";

// 未登陆页面(index)的二级路由
import Product from "../components/FirstPage/Product.vue";
import Service from "../components/FirstPage/Service.vue";
import Login from "../components/FirstPage/Login.vue";
import Register from "../components/FirstPage/Register.vue";

//管理员中心的二级页面
import Home_admin from "../components/admin/Function/Home_admin.vue";
import Audit_user from "../components/admin/Function/Audit_user.vue";
import View_project from "../components/admin/Function/View_project.vue";
import View_user from "../components/admin/Function/View_user.vue";
import Feedback_user from "../components/admin/Function/Feedback_user.vue";
import View_refer from "../components/admin/Function/View_refer.vue";

//审核用户
import detail_user from "../components/admin/Function/audit_user/detail_user.vue";
import audit_list from "../components/admin/Function/audit_user/audit_list.vue";

//查看用户
import normal from "../components/admin/Function/view_user/normal";
import abnormal from "../components/admin/Function/view_user/abnormal";
import view_detail from "../components/admin/Function/view_user/view_detail";

//查看反馈信息
import feedback_list from "../components/admin/Function/feedback_user/feedback_list";
import feedback_detail from "../components/admin/Function/feedback_user/feedback_detail";


//个人中心的二级页面
import Home from "../components/User/Function/Home.vue";
import NewProject from "../components/User/Function/NewProject";
import MyProject from "../components/User/Function/MyProject.vue";
import Refer from "../components/User/Function/Refer.vue";
import Feedback from "../components/User/Function/Feedback.vue";
import PersonInfo from "../components/User/Function/PersonInfo.vue";
import ViewPJ from "../components/User/Function/ViewPJ.vue";

//新建项目的步骤条
import step1 from "../components/User/Function/newpjStep/step1.vue";
import step2 from "../components/User/Function/newpjStep/step2.vue";
import step3 from "../components/User/Function/newpjStep/step3.vue";
import step4 from "../components/User/Function/newpjStep/step4.vue";
import step5 from "../components/User/Function/newpjStep/step5.vue";
import step6 from "../components/User/Function/newpjStep/step6.vue";

//个人信息
import myinfo from "../components/User/Function/Info/myinfo.vue";
import editinfo from "../components/User/Function/Info/editinfo.vue";

//反馈信息
import feedbacklist from "../components/User/Function/feed/feedbacklist.vue";
import addfeedback from "../components/User/Function/feed/addfeedback.vue";
import fbdetail from "../components/User/Function/feed/fbdetail.vue";
//我的项目
import successpj from "../components/User/Function/mypj/successpj.vue";
import unsuccesspj from "../components/User/Function/mypj/unsuccesspj.vue";

//
import view from "../components/User/Function/viewpj/view.vue";
import detail from "../components/User/Function/viewpj/detail.vue";

//易损性数据库
import viewdb from "../components/User/Function/refer/viewdb.vue";
import newdb from "../components/User/Function/refer/newdb/newdb.vue";
//新建易损性数据库
import general_info from "../components/User/Function/refer/newdb/general_info";
import statenum from "../components/User/Function/refer/newdb/statenum";
import consequence from "../components/User/Function/refer/newdb/consequence";
import damage_state from "../components/User/Function/refer/newdb/damage_state";
//generalinfo部分
import generalinfo from "../components/User/Function/refer/newdb/generalinfo/generalinfo";
import notes from "../components/User/Function/refer/newdb/generalinfo/notes";
//consequence部分
import gen_con_info from "../components/User/Function/refer/newdb/consequence/gen_con_info";
import others from "../components/User/Function/refer/newdb/consequence/others.vue";
import re_cost from "../components/User/Function/refer/newdb/consequence/re_cost";
import re_time from "../components/User/Function/refer/newdb/consequence/re_time";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index,
      children:[
        {
          path: '/product',
          name: "product",
          component: Product
        }, {
          path: '/service',
          name: "service",
          component: Service
        },{
          path: '/login',
          name: "login",
          component:Login,
        },
        {
          path: '/register',
          name: "register",
          component: Register,
        }
      ]
    },
    {
      path:'/dashboard',
      name:'dashboard',
      component: Dashboard,
      redirect: '/home',
      children: [
        {
          path: '/home',
          name: "home",
          component: Home
        }, {
          path: '/newpj',
          name: "newpj",
          component: NewProject,
          redirect:'/newpj/step1',
          children: [
            {
              path: '/newpj/step1',
              name: 'step1',
              component: step1,
               meta: {
              //   //keepAlive: true // 需要被缓存
               }
            },
            {
              path: '/newpj/step2',
              name: 'step2',
              component: step2,
              // meta: {
              //  // keepAlive: true // 需要被缓存
              // }
            },
            {
              path: '/newpj/step3',
              name: 'step3',
              component: step3,
              // meta: {
              //  // keepAlive: true // 需要被缓存
              // }
            },
            {
              path: '/newpj/step4',
              name: 'step4',
              component: step4,
              // meta: {
              //  // keepAlive: true // 需要被缓存
              // }
            },
            {
              path: '/newpj/step5',
              name: 'step5',
              component: step5,
              // meta: {
              // //  keepAlive: true // 需要被缓存
              // }
            },
            {
              path: '/newpj/step6',
              name: 'step6',
              component: step6,
              // meta: {
              // //  keepAlive: true // 需要被缓存
              // }
            }
          ]
        }, {
          path: '/mypj',
          name: "mypj",
          component: MyProject,
          redirect:'/mypj/successpj',
          children:[
            {
              path:'/mypj/successpj',
              name:'successpj',
              component:successpj
            },
            {
              path:'/mypj/unsuccesspj',
              name:'unsuccesspj',
              component:unsuccesspj
            },
            
          ]
        },
        {
          path: '/refer',
          name: "refer",
          component: Refer,
          redirect: '/refer/viewdb',
          children:[
            {
              path:'/refer/viewdb',
              name:'viewdb',
              component:viewdb
            },
            {
              path:'/refer/newdb/newdb',
              name:'newdb',
              component:newdb,
              redirect: '/refer/newdb/general_info',
              children:[
                {
                  path:'/refer/newdb/consequence',
                  name:'consequence',
                  component:consequence,
                  redirect:'/refer/newdb/consequence/gen_con_info',
                  children:[
                    {
                      path:'/refer/newdb/consequence/gen_con_info',
                      name:'gen_con_info',
                      component:gen_con_info
                    },
                    {
                      path:'/refer/newdb/consequence/others',
                      name:'others',
                      component:others
                    },
                    {
                      path:'/refer/newdb/consequence/re_cost',
                      name:'re_cost',
                      component:re_cost
                    },
                    {
                      path:'/refer/newdb/consequence/re_time',
                      name:'re_time',
                      component:re_time
                    }
                  ]
                },
                {
                  path:'/refer/newdb/general_info',
                  name:'general_info',
                  component:general_info,
                  redirect:'/refer/newdb/generalinfo/generalinfo',
                  children:[
                    {
                      path:'/refer/newdb/generalinfo/generalinfo',
                      name:'generalinfo',
                      component:generalinfo
                    },
                    {
                      path:'/refer/newdb/generalinfo/notes',
                      name:'notes',
                      component:notes
                    }
                  ]
                },
                {
                  path:'/refer/newdb/damage_state',
                  name:'damage_state',
                  component:damage_state
                },
                {
                  path:'/refer/newdb/statenum',
                  name:'statenum',
                  component:statenum
                }
              ]
            },
          ]
        },
        {
          path:"/feedbk",
          name:'feedbk',
          component:Feedback,
          redirect:'/feedbk/feedbacklist',
          children:[
            {
              path:'/feedbk/feedbacklist',
              name:'feedbacklist',
              component:feedbacklist
            },
            {
              path:'/feedbk/addfeedback',
              name:'addfeedback',
              component:addfeedback
            },
            {
              path:'/feedbk/fbdetail',
              name:'fbdetail',
              component:fbdetail
            }
          ]
        },
        {
          path: "/userinfo",
          name: 'userinfo',
          component: PersonInfo,
          redirect:'/userinfo/myinfo',
          children:[
            {
              path:'/userinfo/myinfo',
              name:'myinfo',
              component:myinfo
            },
            {
              path:'/userinfo/editinfo',
              name:'editinfo',
              component:editinfo
            }
          ]
        },
        {
          path: "/viewPJ",
          name: 'viewPJ',
          component: ViewPJ,
          redirect:"/viewpj/view",
          children:[
            {
              path:'/viewpj/detail',
              name:'detail',
              component:detail
            },
            {
              path:'/viewpj/view',
              name:'view',
              component:view
            }
          ]
        },
      ]
    },
    {
      path:'/dashboard_admin',
      name:'dashboard_admin',
      component:Dashboard_admin,
      redirect:'/home_admin',
      children:[
        {
            path:'/home_admin',
            name:'home_admin',
            component:Home_admin,
        },
        {
          path:'/audit_user',
          name:'audit_user',
          component:Audit_user,
          redirect:'/audit_user/audit_list',
          children:[
            {
              path:'/audit_user/detail_user',
              name:'detail_user',
              component:detail_user
            },
            {
              path:'/audit_user/audit_list',
              name:'audit_list',
              component:audit_list
            }
          ]
        },
        {
          path:'/view_project',
          name:'view_project',
          component:View_project
        },
        {
          path:'/view_user',
          name:'view_user',
          component:View_user,
          redirect: '/view_user/normal',
          children: [
            {
              path:'/view_user/normal',
              name: 'normal',
              component: normal,
            },
            {
              path: '/view_user/abnormal',
              name: 'abnormal',
              component: abnormal
            },
            {
              path: '/view_user/view_detail',
              name: 'view_detail',
              component: view_detail
            }
          ]
        },
        {
          path:'/feedback_user',
          name:'feedback_user',
          component:Feedback_user,
          redirect:'/feedback_user/feedback_list',
          children:[
            {
              path:'/feedback_user/feedback_list',
              name:'feedback_list',
              component:feedback_list,
            },
            {
              path:'/feedback_user/feedback_detail',
              name:'feedback_detail',
              component:feedback_detail,
            }
          ]
        },
        {
          path:'/view_refer',
          name:'view_refer',
          component:View_refer
        }
      ]
    }
  ]
})
          
          
