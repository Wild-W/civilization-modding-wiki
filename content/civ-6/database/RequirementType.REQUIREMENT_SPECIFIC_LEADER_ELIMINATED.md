---
tags:
- RequirementType
title: REQUIREMENT_SPECIFIC_LEADER_ELIMINATED
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_SPECIFIC_LEADER_ELIMINATED
>
> * Class: `ANY`
> * Arguments:
>	* LeaderType `String`
>		* [Leaders.LeaderType]

## Samples

```SQL {title="VIENNA_ELIMINATED"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"VIENNA_ELIMINATED",
		"REQUIREMENT_SPECIFIC_LEADER_ELIMINATED"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"VIENNA_ELIMINATED",
		"LeaderType",
		"LEADER_MINOR_CIV_VIENNA"
	);
	
```
