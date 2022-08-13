---
tags:
- RequirementType
title: REQUIREMENT_OPPONENT_IS_STRONGER
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_OPPONENT_IS_STRONGER
>
> * Class: `Unknown`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_COMBAT_AGAINST_STRONGER_UNIT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_COMBAT_AGAINST_STRONGER_UNIT",
		"REQUIREMENT_OPPONENT_IS_STRONGER"
	);

```
