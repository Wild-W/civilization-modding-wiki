---
tags:
- RequirementType
title: REQUIREMENT_UNIT_TAG_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_UNIT_TAG_MATCHES
>
> * Class: `UNITS`
> * Arguments:
>	* Tag `String`

## Samples

```SQL {title="REQUIREMENT_UNIT_IS_HETAIROI"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIREMENT_UNIT_IS_HETAIROI",
		"REQUIREMENT_UNIT_TAG_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIREMENT_UNIT_IS_HETAIROI",
		"Tag",
		"CLASS_HETAIROI"
	);
	```
