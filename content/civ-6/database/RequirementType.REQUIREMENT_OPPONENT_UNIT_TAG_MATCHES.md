---
tags:
- RequirementType
title: REQUIREMENT_OPPONENT_UNIT_TAG_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_OPPONENT_UNIT_TAG_MATCHES
>
> * Class: `UNITS`
> * Arguments:
>	* Tag `String`

## Samples

```SQL {title="ANTI_CAVALRY_OPPONENT_REQUIREMENT_HC"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"ANTI_CAVALRY_OPPONENT_REQUIREMENT_HC",
		"REQUIREMENT_OPPONENT_UNIT_TAG_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"ANTI_CAVALRY_OPPONENT_REQUIREMENT_HC",
		"Tag",
		"CLASS_HEAVY_CAVALRY"
	);
	
```
