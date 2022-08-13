---
tags:
- RequirementType
title: REQUIREMENT_TEAM_DOMINATION_VICTORY
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_TEAM_DOMINATION_VICTORY
>
> * Class: `TEAMS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="CONQUEST_VICTORY_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"CONQUEST_VICTORY_REQUIREMENT",
		"REQUIREMENT_TEAM_DOMINATION_VICTORY"
	);

```
