---
tags:
- EffectType
title: EFFECT_PLAYER_DIPLOMACY_AGENDA_COMPARE_ARMY_SIZE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_PLAYER_DIPLOMACY_AGENDA_COMPARE_ARMY_SIZE
>
> * Class: `Unknown`
> * Parameters:
>	* AdjustPerStep `Unknown`
>	* DeltaUnits `Unknown`
>	* MaxSteps `Unknown`
>	* MinUnitsNeeded `Unknown`
>	* StatementKey `Unknown`

## Samples

```SQL {title="AGENDA_AMBIORIX_ARMY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_AMBIORIX_ARMY",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_AMBIORIX_ARMY",
		"ON_TURN_STARTED",
		"PLAYER_IS_MAJOR_CIV"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_AMBIORIX_ARMY",
		"AdjustPerStep",
		4
	),
	(
		"AGENDA_AMBIORIX_ARMY",
		"DeltaUnits",
		5
	),
	(
		"AGENDA_AMBIORIX_ARMY",
		"MaxSteps",
		4
	),
	(
		"AGENDA_AMBIORIX_ARMY",
		"MinUnitsNeeded",
		5
	),
	(
		"AGENDA_AMBIORIX_ARMY",
		"StatementKey",
		"AGENDA_AMBIORIX"
	);
	
```

