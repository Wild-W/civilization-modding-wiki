---
tags:
- RequirementType
title: REQUIREMENT_OPPONENT_IS_WOUNDED
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_OPPONENT_IS_WOUNDED
>
> * Class: `UNITS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_OPPONENT_IS_WOUNDED"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_OPPONENT_IS_WOUNDED",
		"REQUIREMENT_OPPONENT_IS_WOUNDED"
	);


```
