---
tags:
- RequirementType
title: REQUIREMENT_TEAM_HAS_HIGHEST_SCORE
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_TEAM_HAS_HIGHEST_SCORE
>
> * Class: `TEAMS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="VICTORY_SCORE_TEAM_HAS_HIGHEST_SCORE"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"VICTORY_SCORE_TEAM_HAS_HIGHEST_SCORE",
		"REQUIREMENT_TEAM_HAS_HIGHEST_SCORE"
	);


```
