import type { SurveyQuestion } from "./SurveyQuestion";

export type Survey = {
    uid: string;
    questions: SurveyQuestion[];
};