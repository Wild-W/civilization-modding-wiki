---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_MAGNIFICENCES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_MAGNIFICENCES
>
> * Class: `Unknown`
> * Parameters:
>	* StatementKey `Unknown`

## Samples
```SQL {title="AGENDA_MAGNIFICENCES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_MAGNIFICENCES",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_MAGNIFICENCES",
		"ON_TURN_STARTED",
		"PLAYER_IS_MAJOR_CIV_KNOWN_10_TURNS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_MAGNIFICENCES",
		"StatementKey",
		"LOC_PLACEHOLDER"
	);
	
```

