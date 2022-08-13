---
tags:
- RequirementType
title: REQUIREMENT_OPPONENT_IS_MINOR_CIV
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_OPPONENT_IS_MINOR_CIV
>
> * Class: `UNITS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_OPPONENT_IS_MINOR_CIV"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_OPPONENT_IS_MINOR_CIV",
		"REQUIREMENT_OPPONENT_IS_MINOR_CIV"
	);

```
