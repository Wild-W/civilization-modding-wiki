---
tags:
- RequirementType
title: REQUIREMENT_OPPONENT_IS_DISTRICT
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_OPPONENT_IS_DISTRICT
>
> * Class: `UNITS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="COMBAT_IS_NOT_DISTRICT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"COMBAT_IS_NOT_DISTRICT",
		"REQUIREMENT_OPPONENT_IS_DISTRICT",
		1
	);


```
